# from os import link


from brownie import SquirrelNFT
from scripts.helpful_scripts import fundWithLink, getAccount
from web3 import Web3


def main():
    # Get account
    account = getAccount()
    # Find the latest nft owned by account
    squirrel_nft = SquirrelNFT[-1]
    # Fund contract with link
    fundWithLink(squirrel_nft.address, amount=Web3.toWei(0.1, "ether"))
    # Create nft
    create_transaction = squirrel_nft.createSquirrel({"from": account})
    create_transaction.wait(1)
    print("Squirrel NFT created!")
