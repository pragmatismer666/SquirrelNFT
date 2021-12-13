import json

count = 42
tokenuri = []
with open("./assets/tokenuri_list.json", "r") as list:
    tokenuri = json.load(list)
for i in range(count):
    print(tokenuri[i])
