# ************************************************************ #
#  This script reads the metadata.csv file and converts it to  #
#  a json file.                                                #
# ************************************************************ #
import csv, json

firstRow = True

data = {}
nftCount = 0

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
            nftCount += 1

print(f"There are {nftCount} unique NFTs created!")
# Writing the diction into a json file.
with open("./assets/meta.json", "w") as outfile:
    json.dump(data, outfile)
print("metadata.json file was created!")
