from brownie import accounts, config, network, CharitableToken
import json

METADATA = {
    "name": "first metadata",
    "description": "new nft with metadata",
    "image": "https://letsenhance.io/static/8f5e523ee6b2479e26ecc91b9c25261e/1015f/MainAfter.jpg"
}
def main():
    dev = accounts.load("deployment_account")

    charity_token = CharitableToken.deploy(
        dev,
        {'from': dev}
    )

    metadata_json = json.dumps(METADATA)

    charity_token.safeMint(dev, metadata_json, {'from': dev})

    token_id = charity_token.tokenOfOwnerByIndex(dev, 0)

    print("Token contract deployed at:", charity_token.address)
    print("Token ID of the minted NFT:", token_id)