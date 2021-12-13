# ************************************************************ #
#  This script reads the metadata.json file and calculates the #
#  cuteness attribute for the squirrel.                         #
# ************************************************************ #
import json

numAssets = 42

background = {"black": 20, "blue": 30, "green": 40, "orange": 25, "red": 15, "white": 5}
clothes = {"none": 0, "blue_dot": 20}
headgear = {"none": 0, "std_lord": 20}
wristband = {"none": 0, "yellow": 20}

cuteness = 0
cutenessMeta = {}

with open("assets/meta.json", "r") as meta:
    data = json.load(meta)
    for i in range(numAssets):
        cuteness = 0
        for j in data[str(i)]:
            cuteness = (
                background[j["background"]]
                + clothes[j["clothes"]]
                + headgear[j["head_gear"]]
                + wristband[j["wristband"]]
            )
            cutenessMeta[i] = [{"cuteness": cuteness}]
            print(f"Squirrel {i} has a cuteness score of {cuteness}!!")

with open("./assets/cuteness.json", "w") as outfile:
    json.dump(cutenessMeta, outfile)
print("cuteness.json file was created!")


# with open("assets/cuteness.json", "r") as cuteness:
#     cute = json.load(cuteness)
#     for i in cute[str(0)]:
#         print(i["cuteness"])
