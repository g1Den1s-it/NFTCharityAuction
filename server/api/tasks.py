import json
import asyncio
from NFTCharityAuction.celery import app
from web3 import Web3
from websockets import connect
from api.models import NetworkTransaction


@app.task
def get_event_task():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(get_event())


async def get_event():
    async with connect("ws://network:8545") as ws:
        await ws.send(json.dumps({"id": 1, "method": "eth_subscribe", "params": ["newHeads"]}))
        subscription_response = await ws.recv()

        web3 = Web3(Web3.HTTPProvider("http://network:8545"))
        while True:
            try:
                message = await asyncio.wait_for(ws.recv(), timeout=60)
                data_json = json.loads(message)

                block = web3.eth.get_block(data_json["params"]["result"]["hash"])
                transaction_hash = block["transactions"][0].hex()
                transaction = web3.eth.get_transaction(transaction_hash)
                # work with db
                net_transaction = await NetworkTransaction.objects.acreate(
                    hash_block=transaction_hash,
                    from_address=transaction['from'],
                    to_address=transaction['to'],
                    value=str(transaction['value']),
                    gas_price=transaction['gasPrice']
                )
                await net_transaction.asave()
                print("Transaction save success")
            except Exception as e:
                print("error", e)
