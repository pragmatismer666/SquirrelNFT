# ************************************************************ #
#  This program takes the binary data from the images in       #
#  the assets folder and uploads them to the local IFPS        #
#  and generates a list of index to tokenURIs in JSON format.  #
# ************************************************************ #
from pathlib import Path
import requests
import json
import time


assetCount = 42
tokenUriMapping = {}
count = 3


for i in range(assetCount):
    # Build filepath
    filepath = f"./assets/squirrel/squirrel{i}.png"
    with Path(filepath).open("rb") as fp:
        image_binary = fp.read()
        ipfs_url = "http://127.0.0.1:5001"
        endpoint = "/api/v0/add"
        response = requests.post(ipfs_url + endpoint, files={"file": image_binary})
        ipfs_hash = response.json()["Hash"]
        filename = filepath.split("/")[-1:][0]
        image_uri = f"https://ipfs.io/ipfs/{ipfs_hash}?filename={filename}"
        print(image_uri)
        tokenUriMapping[i] = image_uri


with open("./assets/metadata.json", "w") as outfile:
    json.dump(tokenUriMapping, outfile)
    print("Token URI mapping logged!")
