import json
from web3 import Web3
from django.contrib import admin
from django import forms
from .models import MetadataNFT, Auction, RewardList, NetworkTransaction

# Register your models here.


class MetadataNFTForm(forms.ModelForm):
    wallet = forms.CharField(label="your private key", required=True)

    class Meta:
        model = MetadataNFT
        fields = '__all__'


class MetadataNFTAdmin(admin.ModelAdmin):
    form = MetadataNFTForm

    def save_model(self, request, obj, form, change):
        obj.user = request.user

        super().save_model(request, obj, form, change)

        obj.save()

        contract_file_path = 'token/CharitableToken.json'
        wallet = form.cleaned_data['wallet']

        with open(contract_file_path, 'r') as file:
            source = file.read()
            contract_data = json.loads(source)

        abi = contract_data['abi']
        bytecode = contract_data['bytecode']

        web3 = Web3(Web3.HTTPProvider("http://network:8545"))

        if not web3.is_connected():
            return

        dev_account = web3.eth.account.from_key(wallet)

        charity_token = web3.eth.contract(abi=abi, bytecode=bytecode)
        tx_hash = charity_token.constructor(dev_account.address).transact({'from': dev_account.address}).hex()

        tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)

        charity_token = web3.eth.contract(address=tx_receipt.contractAddress, abi=abi)

        url = f"http://0.0.0.0:80/api/v1/{obj.id}/"

        tx_hash = charity_token.functions.safeMint(dev_account.address, obj.id, url).transact({'from': dev_account.address}).hex()

        web3.eth.wait_for_transaction_receipt(tx_hash)


class NetworkTransactionAdmin(admin.ModelAdmin):
    readonly_fields = [field.name for field in NetworkTransaction._meta.fields]


admin.site.register(MetadataNFT, MetadataNFTAdmin)
admin.site.register(Auction)
admin.site.register(NetworkTransaction, NetworkTransactionAdmin)
admin.site.register(RewardList)
