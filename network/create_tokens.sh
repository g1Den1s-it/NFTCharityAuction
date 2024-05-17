#!/bin/sh

brownie pm install OpenZeppelin/openzeppelin-contracts@5.0.0

brownie compile

brownie networks add Ethereum charity host=http://0.0.0.0:8545 chainid=1337

brownie run deploy.py --network charity

ganache-cli --host 0.0.0.0 --port 8545 --chainId 1337