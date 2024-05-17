from brownie import accounts, config, network, CharitableToken, Choken

def main():
    network.connect("charity")
    if network.is_connected():

        dev = accounts.add("0xc15473206fd16df5dbbea53e3b5e2c338f58e8cc35cb1ee3eefde9291a974fa8")

        charity_token = CharitableToken.deploy(
            dev.address,
            {
                'from': dev,
            }
        )
        choken = Choken.deploy(
            dev.address,
            {
                'from': dev,
            }
        )

