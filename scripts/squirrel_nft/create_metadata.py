from brownie import SquirrelNFT, network
from metadata.nft_metadata_template import metadata_template
from scripts.helpful_scripts import getTokenUri, getCuteValue
from pathlib import Path
import requests
import json
import os


def main():
    squirrel_nft = SquirrelNFT[-1]
    nftNum = squirrel_nft.tokenCounter()
    print(f"You have created {nftNum} squirrel NFTs!!")
    for token_id in range(nftNum):
        squirrel_variation = squirrel_nft.tokenIdToVariation(token_id)
        metadata = metadata_template
        metadata_file_name = (
            f"./metadata/{network.show_active()}/{token_id}-squirrel.json"
        )
        if Path(metadata_file_name).exists():
            print(f"{metadata_file_name} already exists! Delete it to overwrite")
        else:
            print(f"Creating Metadata file: {metadata_file_name}")
            # Set the metadata Name
            metadata["name"] = f"squirrel{squirrel_variation}"
            # Set the metadata Description
            metadata[
                "description"
            ] = f"Squirrel{squirrel_variation} reporting for duty!"
            # Retrieve the tokenURI and set the imageuri
            metadata["image"] = getTokenUri(squirrel_variation)
            # Retrieve and set the cuteness attribute
            cute_value = getCuteValue(squirrel_variation)
            metadata["attributes"].append(
                {"trait_type": "cuteness", "value": cute_value}
            )
            # At this point, metadata stores the metadata for the NFT.
            with open(metadata_file_name, "w") as file:
                json.dump(metadata, file)
            # Metadata is now created.
            # uploadToIpfs(metadata_file_name)


def uploadToIpfs(filepath):
    with Path(filepath).open("rb") as fp:
        image_binary = fp.read()
        # upload to uploadToIpfs
        ipfs_url = "http://127.0.0.1:5001"
        endpoint = "/api/v0/add"
        response = requests.post(ipfs_url + endpoint, files={"file": image_binary})
        ipfs_hash = response.json()["Hash"]
        filename = filepath.split("/")[-1:][0]
        image_uri = f"https://ipfs.io/ipfs/{ipfs_hash}?filename={filename}"
        print(image_uri)
        return image_uri
