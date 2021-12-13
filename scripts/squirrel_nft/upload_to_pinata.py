import os
from pathlib import Path
import requests
import json
import time
from brownie import network, config

PINATA_BASE_URL = "https://api.pinata.cloud/"
endpoint = "pinning/pinFileToIPFS"
endpointJson = "pinning/pinJSONToIPFS"
# Change this filepath


headers = {
    "pinata_api_key": str(os.getenv("PINATA_API_KEY")),
    "pinata_secret_api_key": str(os.getenv("PINATA_API_SECRET")),
}

assetcount = 42
hashTable = []
jsonTable = []


def uploadImages():
    for i in range(assetcount):
        filepath = f"./assets/squirrel/squirrel{i}.png"
        filename = filepath.split("/")[-1:][0]
        with Path(filepath).open("rb") as fp:
            image_binary = fp.read()
            response = requests.post(
                PINATA_BASE_URL + endpoint,
                files={"file": (filename, image_binary)},
                headers=headers,
            )
            print(response.json())
            hashTable.append(response.json())


def uploadMetadata():
    activeNetwork = network.show_active()

    for i in range(assetcount):
        with open(f"./metadata/{activeNetwork}/squirrel{i}.json", "r") as file:
            data = json.load(file)
        response = requests.post(PINATA_BASE_URL + endpointJson, data, headers=headers)
        jsonTable.append(response.json())
    with open("./assets/list.json", "w") as outfile:
        json.dump(jsonTable, outfile)


def main():
    # uploadImages()
    uploadMetadata()


if __name__ == "__main__":
    main()

# QmPSSWWzZGqppigVkS9BUJKXqe67aFTkFH6mrKDHBjjv8n
