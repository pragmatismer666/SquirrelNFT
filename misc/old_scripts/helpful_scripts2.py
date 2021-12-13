import json


def getTokenUri(squirrel_number):
    with open("assets/tokenuri.json", "r") as tokenuri:
        data = json.load(tokenuri)
        token_uri = data[str(squirrel_number)]
    return token_uri


def getCuteValue(squirrel_number):
    with open("assets/cuteness.json", "r") as cute_attribute:
        cute_data = json.load(cute_attribute)
        for cute_level in cute_data[str(squirrel_number)]:
            cute_value = cute_level["cuteness"]
    return cute_value
