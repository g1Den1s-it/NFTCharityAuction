from django.contrib import admin
from django import forms
from .models import MetadataNFT, Auction, RewardList, NetworkTransaction

# Register your models here.


class NetworkTransactionAdmin(admin.ModelAdmin):
    readonly_fields = [field.name for field in NetworkTransaction._meta.fields]


admin.site.register(MetadataNFT)
admin.site.register(Auction)
admin.site.register(NetworkTransaction, NetworkTransactionAdmin)
admin.site.register(RewardList)
