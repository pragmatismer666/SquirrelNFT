# ************************************************************************************************* #
#                                                                                                   #
# Squirrel Images and its corresponding metadata have been generated from another program.          #
# See rounakbanik's generative-art-nft library https://github.com/rounakbanik/generative-art-nft    #
#                                                                                                   #
# The following highlights the steps needed to take a folder of images and metadata and             #
# generate tokenURIs through IPFS so that we can set the correct tokenURI for our NFTs.             #
#                                                                                                   #
# Steps:                                                                                            #
# 1. Convert metadata.csv to json.                                                                  #
# 2. Analyze metadata to score the cuteness level and store in json.                                #
# 3. Upload the Squirrel Images to IPFS.                                                            #
# 4. Retrieve image uri for all images on IPFS into json.                                           #
# 5. Build Squirrel metadata with the cuteness and image uri into json.                             #
# 6. Upload the metadata to IPFS.                                                                   #
# 7. Retrieve tokenuri from IPFS as json.                                                           #
# ===> Now we should be able to set the tokenURI with the tokenURI that we have generated.          #
#                                                                                                   #
# ************************************************************************************************* #

import csv, json, requests

from pathlib import Path
import time

# 1. Convert metadata.csv to json.


def convertCsvToJson():

    data = {}
    firstRow = True

    with open("./assets/metadata.csv", newline="") as csvfile:
        file = csv.reader(csvfile, delimiter=",", quotechar="|")
        for row in file:
            if firstRow:
                firstRow = False
            else:
                data[row[0]] = [
                    {
                        "background": row[1],
                        "body": row[2],
                        "eyes": row[3],
                        "head_gear": row[4],
                        "clothes": row[5],
                        "held_item": row[6],
                        "hands": row[7],
                        "wristband": row[8],
                    }
                ]

    with open("./assets/image_metadata.json", "w") as outfile:
        json.dump(data, outfile)
    print("The image metadata .CSV file was successfully converted to JSON")


# 2. Analyze metadata to score the cuteness level and store in json.


def scoreCuteness():
    squirrelCount = getSquirrelCount()
    # Hard coded cuteness scoring criteria. - No real reason as to why things are scored the way they are.
    background = {
        "black": 20,
        "blue": 30,
        "green": 40,
        "orange": 25,
        "red": 15,
        "white": 5,
    }
    clothes = {"none": 0, "blue_dot": 20}
    headgear = {"none": 0, "std_lord": 20}
    wristband = {"none": 0, "yellow": 20}
    cuteness = 0
    cuteJson = {}
    with open("assets/image_metadata.json", "r") as meta:
        data = json.load(meta)
        for i in range(squirrelCount):
            cuteness = 0
            for j in data[str(i)]:
                cuteness = (
                    background[j["background"]]
                    + clothes[j["clothes"]]
                    + headgear[j["head_gear"]]
                    + wristband[j["wristband"]]
                )
                cuteJson[i] = {"cuteness": cuteness}
                print(f"Squirrel {i} has a cuteness score of {cuteness}!!")
    with open("./assets/cuteness_level.json", "w") as outfile:
        json.dump(cuteJson, outfile)
    print("Cuteness values generated!")


# 3. Upload the Squirrel Images to IPFS.


def uploadImagesToIPFS():
    squirrelCount = getSquirrelCount()
    imageUri = []

    for i in range(squirrelCount):
        filepath = f"./assets/squirrel/squirrel{i}.png"
        with Path(filepath).open("rb") as fp:
            image_binary = fp.read()
            ipfs_url = "http://127.0.0.1:5001"
            endpoint = "/api/v0/add"
            response = requests.post(ipfs_url + endpoint, files={"file": image_binary})
            ipfs_hash = response.json()["Hash"]
            filename = filepath.split("/")[-1:][0]
            image_uri = f"https://ipfs.io/ipfs/{ipfs_hash}?filename={filename}"
            imageUri.append({"name": f"squirrel{i}", "image_uri": image_uri})
            time.sleep(1)

    # 4. Retrieve image uri for all images on IPFS into json.
    with open("./assets/imageuri.json", "w") as outfile:
        json.dump(imageUri, outfile)
    print("Images successfully uploaded to IPFS!")


# 5. Build Squirrel metadata with the cuteness and image uri into json.


def buildSquirrelMetadata():
    squirrelCount = getSquirrelCount()
    cuteness = getCutenessList()
    imageUriList = getImageUriList()
    for i in range(squirrelCount):
        metadata = []
        name = imageUriList[i]["name"]
        description = f"Squirrel{i} reporting for duty!"
        image_uri = imageUriList[i]["image_uri"]
        cute_level = cuteness[str(i)]["cuteness"]
        data = {
            "name": name,
            "description": description,
            "image": image_uri,
            "attributes": [{"trait_type": "cuteness", "value": cute_level}],
        }
        metadata.append(data)
        with open(f"./metadata/squirrel/{name}.json", "w") as outfile:
            json.dump(metadata, outfile)
    print("Squirrel Metadata successfully built.")


# 6. Upload the metadata to IPFS.


def uploadMetadata():
    squirrelCount = getSquirrelCount()
    tokenUri = []
    for i in range(squirrelCount):
        filepath = f"./metadata/squirrel/squirrel{i}.json"
        with Path(filepath).open("rb") as fp:
            image_binary = fp.read()
            ipfs_url = "http://127.0.0.1:5001"
            endpoint = "/api/v0/add"
            response = requests.post(ipfs_url + endpoint, files={"file": image_binary})
            ipfs_hash = response.json()["Hash"]
            filename = filepath.split("/")[-1:][0]
            token_uri = f"https://ipfs.io/ipfs/{ipfs_hash}?filename={filename}"
            tokenUri.append({"name": f"squirrel{i}", "token_uri": token_uri})
            time.sleep(1)
    print("TokenURI successfully uploaded to IPFS!")
    with open("./assets/tokenuri_list.json", "w") as outfile:
        json.dump(tokenUri, outfile)
    print("Created TokenURI list.")


# 7. Retrieve tokenuri from IPFS as json.


def getTokenUriList():
    with open("./assets/tokenuri_list.json", "r") as outfile:
        return json.load(outfile)


# *********************
# * Helpful functions *
# *********************
def getSquirrelCount():
    with open("./assets/meta.json", "r") as meta:
        m = json.load(meta)
        return len(m)


def getCutenessList():
    with open("./assets/cuteness_level.json", "r") as cute_level:
        return json.load(cute_level)


def getImageUriList():
    with open("./assets/imageuri.json", "r") as imageuri:
        return json.load(imageuri)
