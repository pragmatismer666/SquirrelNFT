from scripts.helpful_scripts import (
    getAccount,
    OPENSEA_URL,
    getContract,
    fundWithLink,
)
from brownie import SquirrelNFT, network, config


def deployAndCreate():
    # ************************************
    # * 1. Deploy contract               *
    # ************************************
    account = getAccount()
    squirrel_NFT = SquirrelNFT.deploy(
        getContract("vrf_coordinator"),
        getContract("link_token"),
        config["networks"][network.show_active()]["keyhash"],
        config["networks"][network.show_active()]["fee"],
        {"from": account},
    )

    # ************************************
    # * 2. Fund contract with LINK       *
    # ************************************
    fundWithLink(squirrel_NFT.address)

    # ************************************
    # * 3. Create NFT                    *
    # ************************************
    create_tx = squirrel_NFT.createSquirrel({"from": account})
    create_tx.wait(1)
    print("New Token has been created!")
    return squirrel_NFT, create_tx


def main():
    deployAndCreate()
