import json

count = 42

# https://ipfs.io/ipfs/QmcwSacsa28wfHhhuV47Cc7kbS3ZnHdQTiExRt9C7ooN4A?filename=squirrel0.json

tokenuri_list = []

# with open("./assets/tokenuri.json", "r") as uri:
#     data = json.load(uri)
#     tokenuri_list.append(data)

# for i in range(count):
#     name = tokenuri_list[0][i]["Name"]
#     with open(f"./assets/tokenuri/{name}", "w") as sq:
#         json.dump(tokenuri_list[0][i], sq)

# tokenuri_list = []
# i = 0

# for i in range(count):
#     with open(f"./assets/tokenuri/squirrel{i}.json", "r") as file:
#         data = json.load(file)
#         tokenuri_list.append(data)

# with open("./assets/tokenuri_list.json", "w") as file:
#     json.dump(tokenuri_list, file)

with open("./assets/list.json", "r") as meta:
    data = json.load(meta)
    for i in range(count):
        hash = data[i]["IpfsHash"]
        tokenuri = f"ipfs://{hash}"
        tokenuri_list.append(tokenuri)

with open("./assets/tokenuri_list.json", "w") as outfile:
    json.dump(tokenuri_list, outfile)
