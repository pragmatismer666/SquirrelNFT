from brownie import accounts, network, config, LinkToken, VRFCoordinatorMock, Contract
from web3 import Web3
import json

LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache", "mainnet-fork"]
OPENSEA_URL = "https://testnets.opensea.io/assets/{}/{}"


def getAccount(index=None, id=None):
    if index:
        return accounts[index]
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        return accounts[0]
    if id:
        return accounts.load(id)
    return accounts.add(config["wallets"]["from_key"])


contract_to_mock = {"link_token": LinkToken, "vrf_coordinator": VRFCoordinatorMock}


def getContract(contract_name):
    contract_type = contract_to_mock[contract_name]
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        if len(contract_type) <= 0:
            deployMocks()
        contract = contract_type[-1]
    else:
        contract_address = config["networks"][network.show_active()][contract_name]
        contract = Contract.from_abi(
            contract_type._name, contract_address, contract_type.abi
        )
    return contract


def deployMocks():
    print(f"The active network is {network.show_active()}")
    print("Deploying mocks...")
    account = getAccount()
    print("Deploying Mock LinkToken...")
    link_token = LinkToken.deploy({"from": account})
    print(f"Link Token deployed to {link_token.address}")
    print("Deploying Mock VRF Coordinator...")
    vrf_coordinator = VRFCoordinatorMock.deploy(link_token.address, {"from": account})
    print(f"VRFCoordinator deployed to {vrf_coordinator.address}")
    print("All done!")


def fundWithLink(
    contract_address, account=None, link_token=None, amount=Web3.toWei(0.3, "ether")
):
    account = account if account else getAccount()
    link_token = link_token if link_token else getContract("link_token")
    funding_tx = link_token.transfer(contract_address, amount, {"from": account})
    funding_tx.wait(1)
    print(f"Funded {contract_address}")
    return funding_tx


def getCuteValue(squirrel_number):
    with open("assets/cuteness.json", "r") as cute_attribute:
        cute_data = json.load(cute_attribute)
        for cute_level in cute_data[str(squirrel_number)]:
            cute_value = cute_level["cuteness"]
    return cute_value


def getMetaUri(squirrel_number):
    with open("assets/metauri.json", "r") as metanuri:
        data = json.load(metanuri)
        token_uri = data[str(squirrel_number)]
    return token_uri


def getTokenUriList():
    with open("./assets/tokenuri_list.json", "r") as outfile:
        return json.load(outfile)
