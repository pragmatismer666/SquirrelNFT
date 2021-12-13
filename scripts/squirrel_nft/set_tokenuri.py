from brownie import network, SquirrelNFT
from scripts.helpful_scripts import (
    OPENSEA_URL,
    getAccount,
    getTokenUriList,
)
import json


def set_tokenURI(token_id, nft_contract, tokenURI):
    account = getAccount()
    tx = nft_contract.setTokenURI(token_id, tokenURI, {"from": account})
    tx.wait(1)
    print(
        f"You can view your NFT at {OPENSEA_URL.format(nft_contract.address, token_id)} !"
    )
    print("Please wait up to 20 minutes, and hit the refresh metadata button!")


def set_tokenURI(token_id, nft_contract, tokenURI):
    account = getAccount()
    tx = nft_contract.setTokenURI(token_id, tokenURI, {"from": account})
    tx.wait(1)
    print(
        f"You can view your NFT at {OPENSEA_URL.format(nft_contract.address, token_id)} !"
    )
    print("Please wait up to 20 minutes, and hit the refresh metadata button!")


def main():
    print(f"Working on {network.show_active()}")
    squirrelnft = SquirrelNFT[-1]
    number_of_squirrels = squirrelnft.tokenCounter()
    print(f"You have {number_of_squirrels} tokenIds")
    tokenuri_list = getTokenUriList()
    for token_id in range(number_of_squirrels):
        if not squirrelnft.tokenURI(token_id).startswith("https://"):
            print(f"Setting tokenURI of Squirrel{token_id}")
            squirrel_number = squirrelnft.tokenIdToVariation[token_id]
            squirrel_token_uri = tokenuri_list(squirrel_number)
            set_tokenURI(token_id, squirrelnft, squirrel_token_uri)
