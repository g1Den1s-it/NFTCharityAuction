from brownie import accounts, config, network, CharitableToken

def main():
    dev = accounts.load('deployment_account')

    charity_token = CharitableToken.deploy(
        dev.address,
        {'from': dev}
    )
    return charity_token