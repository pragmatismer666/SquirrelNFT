# This version of the create_metadata script uses the sys library to find the nft_metadata_template file from the metadata folder while
# being called from a different folder. This requires the exact path that needs to be added, thus not making it useful when uploading it
# online. This is only for testing the creation of the metadata using the metadata template.
import json

# metadata_file_name = "0-squirrel2.json"
# meta = metadata_template
# squirrel_variation = 2
# print(f"Creating Metadata file: {metadata_file_name}")
# # Set the metadata Name
# meta["name"] = f"squirrel{squirrel_variation}"
# # Set the metadata Description
# meta["description"] = f"Squirrel{squirrel_variation} reporting for duty!"
# # Retrieve the tokenURI and set the imageuri
# image_uri = ""
# with open("assets/tokenuri.json", "r") as tokenuri:
#     data = json.load(tokenuri)
#     meta["image"] = data[str(squirrel_variation)]
#     # Retrieve and set the cuteness attribute
# with open("assets/cuteness.json", "r") as cute_attribute:
#     cute_data = json.load(cute_attribute)
#     for cute_level in cute_data[str(squirrel_variation)]:
#         cute_value = cute_level["cuteness"]
#     meta["attributes"].append({"trait_type": "cuteness", "value": cute_value})
# print(meta)
# with open(f"./metadata/{metadata_file_name}", "w") as outfile:
#     json.dump(meta, outfile)

assetNum = 42
metadata = []
data = {}
# Access the Imageuri.json file to retrieve the image uri and build most of the metadata for each squirrel.
with open("./assets/imageuri.json", "r") as file:
    j = json.load(file)
    for i in range(assetNum):
        # Name
        name = j[i]["name"]
        # Description
        description = f"Squirrel{i} reporting for duty!"
        # Image URI
        image_uri = j[i]["imageuri"]
        # Attributes
        data = {
            "name": name,
            "description": description,
            "image": image_uri,
            "attributes": [{"trait_type": "cuteness", "value": -1}],
        }
        metadata.append(data)

# Access the cuteness.json file to update each squirrel with its cuteness attribute value.
with open("./assets/cuteness.json", "r") as file:
    c = json.load(file)
    for index in range(assetNum):
        cute_level = c[str(index)][0]["cuteness"]
        metadata[index]["attributes"][0]["value"] = cute_level

# Dump metadata into json file.
# with open("./assets/tokenuri.json", "w") as file:
#     json.dump(metadata, file)

i = 0
for i in range(assetNum):
    filename = f"squirrel{i}"
    with open(f"./metadata/rinkeby/{filename}.json", "w") as file:
        json.dump(metadata[i], file)
        continue
