import requests
import json


count = 42
RINKEBY = "QmREj8foyqJ6fGW6r7SF4NoNujaWmaSV9y486DxNrJSWyq"

ipfs_url = "http://127.0.0.1:5001"
endpoint = f"/api/v0/file/ls?arg={RINKEBY}"
response = requests.post(ipfs_url + endpoint)
# print(response.content)
r = response.content.decode()
rs = json.loads(r)
tokenuri_list = rs["Objects"][RINKEBY]["Links"]
with open("./assets/tokenuri.json", "w") as file:
    json.dump(tokenuri_list, file)
