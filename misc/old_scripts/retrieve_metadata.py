import json

count = 42
metadata = []

# for i in range(count):
#     with open(f"./metadata/rinkeby/squirrel{i}.json", "r") as file:
#         data = json.load(file)
#         metadata.append(data)

# with open("./assets/metadata.json", "w") as meta:
#     json.dump(metadata, meta)

with open("./assets/metadata.json", "r") as meta:
    data = json.load(meta)
    squirrel = data[20]
    print("Name: " + squirrel["name"])
    print("Description" + squirrel["description"])
    print("Image URI" + squirrel["image"])
    print(
        squirrel["attributes"][0]["trait_type"]
        + " "
        + str(squirrel["attributes"][0]["value"])
    )
