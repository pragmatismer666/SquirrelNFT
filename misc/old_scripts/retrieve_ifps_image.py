import requests
import json

# SQUIRREL_LIBRARY = "QmZVzEmMV8VjMnLVUGYV6ygFnAGk2Efw1JQVwmyieZgrNL"

# ipfs_url = "http://127.0.0.1:5001"
# endpoint = f"/api/v0/file/ls?arg={SQUIRREL_LIBRARY}"
# response = requests.post(ipfs_url + endpoint)
# # print(response.content)
# r = response.content.decode()
# rs = json.loads(r)
# tokenuri_list = rs["Objects"][SQUIRREL_LIBRARY]["Links"]


hashTable = [
    {
        "IpfsHash": "QmbJ8GB2AqzseZDqtWdXHba8HG9oXo1hs6NpkPut6fkLSQ",
        "PinSize": 55930,
        "Timestamp": "2021-11-30T00:21:50.299Z",
    },
    {
        "IpfsHash": "QmZwyHEoHuoRj1w7XgQ9Tiag8duS5NJm818byCJ83NsAVK",
        "PinSize": 58939,
        "Timestamp": "2021-11-30T00:21:50.984Z",
    },
    {
        "IpfsHash": "QmPSSWWzZGqppigVkS9BUJKXqe67aFTkFH6mrKDHBjjv8n",
        "PinSize": 56715,
        "Timestamp": "2021-11-30T00:21:51.716Z",
    },
    {
        "IpfsHash": "QmYMLCfuxP6YP9y7noDAJV3KzVJjmsTyqmh57uT8XRKczy",
        "PinSize": 56830,
        "Timestamp": "2021-11-30T00:21:53.282Z",
    },
    {
        "IpfsHash": "QmPtBvuwqpWSNBeCJejrzpv1XFqjauySAjwPZNciijXVKM",
        "PinSize": 57836,
        "Timestamp": "2021-11-30T00:21:54.050Z",
    },
    {
        "IpfsHash": "QmcZhLyun8D3TEWBLwostHbxt2SWYukZP63yQrdQi2beaV",
        "PinSize": 56637,
        "Timestamp": "2021-11-30T00:21:54.709Z",
    },
    {
        "IpfsHash": "QmfDoDo5ASZHV8LxmtNTFngjeVyTjZMToRH83QXi1o8bSF",
        "PinSize": 50802,
        "Timestamp": "2021-11-30T00:21:55.384Z",
    },
    {
        "IpfsHash": "Qmcwo9tsoadSFGhrB3aZXBH887jMpoXwTwjtq9nzXsFcpf",
        "PinSize": 58836,
        "Timestamp": "2021-11-30T00:21:56.043Z",
    },
    {
        "IpfsHash": "QmZpjSaUrFpUezzbyDk9ka7hGfLepVLo5WW7kG3qXnXbng",
        "PinSize": 56800,
        "Timestamp": "2021-11-30T00:21:56.660Z",
    },
    {
        "IpfsHash": "QmVLF74fQkBnazppCyKQM8TV1YFbTh7QwjEEicKRu4yABJ",
        "PinSize": 56658,
        "Timestamp": "2021-11-30T00:21:57.296Z",
    },
    {
        "IpfsHash": "QmXUr9de4HwscWQhbPfUsMcZJEqGfr6k8ULS3SgUcQtnAj",
        "PinSize": 48061,
        "Timestamp": "2021-11-30T00:21:57.950Z",
    },
    {
        "IpfsHash": "QmZwjhwfJxWBcZz7vrgAJB38n9wGhqEvjHajdmz7pm3JAp",
        "PinSize": 58086,
        "Timestamp": "2021-11-30T00:21:58.603Z",
    },
    {
        "IpfsHash": "QmV2V6zxwfdAFr3wxzTak3Y58baM3G2goJjPyi1DaesdHH",
        "PinSize": 57363,
        "Timestamp": "2021-11-30T00:21:59.276Z",
    },
    {
        "IpfsHash": "QmVjegJaQQG74KWymH6AUiTCUXdLX7KJ2rr2WRPaLdCUYV",
        "PinSize": 56758,
        "Timestamp": "2021-11-30T00:21:59.852Z",
    },
    {
        "IpfsHash": "QmUXs6v1D2Xz5hbr1Bism3cV4SoNiiT9ZzDz6aZK2cpChe",
        "PinSize": 50084,
        "Timestamp": "2021-11-30T00:22:00.496Z",
    },
    {
        "IpfsHash": "QmVFCTQXTme43oviQRDNTCpxDmWM1jEzg72jA1eCgxuvah",
        "PinSize": 57151,
        "Timestamp": "2021-11-30T00:22:01.120Z",
    },
    {
        "IpfsHash": "QmecgNwZXJdWhnkxhjKQePqF42gHVoAcUhEWJs7Y5yNY7T",
        "PinSize": 58302,
        "Timestamp": "2021-11-30T00:22:01.833Z",
    },
    {
        "IpfsHash": "QmZPkkugn6615HCoJ9qsk1knTuTcyuznAZTFJuQhPHMe6F",
        "PinSize": 58738,
        "Timestamp": "2021-11-30T00:22:02.481Z",
    },
    {
        "IpfsHash": "QmSTrtCYK13PKeJHePd7u9gi2f4P7y4MjHG9w7nN6S16Ao",
        "PinSize": 57472,
        "Timestamp": "2021-11-30T00:22:03.110Z",
    },
    {
        "IpfsHash": "QmSWz6U2aPo7L5Yka1bA3Q2xoxr3V7Yay6oCJQfTn9ePyR",
        "PinSize": 56940,
        "Timestamp": "2021-11-30T00:22:03.741Z",
    },
    {
        "IpfsHash": "QmdLKJvpn96tautzvv2EoCyALu5r1kFr6HC9DgcFsSQfUa",
        "PinSize": 57405,
        "Timestamp": "2021-11-30T00:22:04.441Z",
    },
    {
        "IpfsHash": "QmP87EQdutA7neYgKi3JbHr6ctHm4gbPtLcnwQYTo8fuAJ",
        "PinSize": 58192,
        "Timestamp": "2021-11-30T00:22:05.055Z",
    },
    {
        "IpfsHash": "QmR1ZUxUJGQWMVmcT3SUG3ie9ugjyN7a3VNcPgGXS5744P",
        "PinSize": 56322,
        "Timestamp": "2021-11-30T00:22:05.671Z",
    },
    {
        "IpfsHash": "QmShSj1CgWmiSyUAjquHyciySGAszJCFqRXbM2nxuxTFiQ",
        "PinSize": 58096,
        "Timestamp": "2021-11-30T00:22:06.284Z",
    },
    {
        "IpfsHash": "QmP35KqttLqtGdkEUT3BcX6B3QT7wN7bhUHoPbfGPfUbZs",
        "PinSize": 58877,
        "Timestamp": "2021-11-30T00:22:06.884Z",
    },
    {
        "IpfsHash": "QmUYsv8sT9rvRuVmA5sXq6T2zdPMXHFPX6ZnpVS9VDHpar",
        "PinSize": 56561,
        "Timestamp": "2021-11-30T00:22:07.493Z",
    },
    {
        "IpfsHash": "QmPDthG2VMjqqX1G8AjT8Wgc9Wwy61wDbw72ZVDkPGDAr4",
        "PinSize": 56181,
        "Timestamp": "2021-11-30T00:22:08.466Z",
    },
    {
        "IpfsHash": "Qmb2kQNEVC2Y4H4UfckP7uNuQXiPA3Dw1G5wCCGuhHE3wo",
        "PinSize": 57323,
        "Timestamp": "2021-11-30T00:22:09.137Z",
    },
    {
        "IpfsHash": "QmZXwQjTkYneewcJv94gfKYW2LJgxiybKiW4JSrqtf1X1J",
        "PinSize": 58248,
        "Timestamp": "2021-11-30T00:22:09.918Z",
    },
    {
        "IpfsHash": "QmfVkNR7qUjHxQWWu1kv6hR2xh9hLKJQigfaSXyWDYvqFX",
        "PinSize": 57249,
        "Timestamp": "2021-11-30T00:22:10.597Z",
    },
    {
        "IpfsHash": "QmbfzgfkdZrXhQ1RwRqMe86KXeB9BPXdRCynoZeF7MCqzd",
        "PinSize": 50219,
        "Timestamp": "2021-11-30T00:22:11.215Z",
    },
    {
        "IpfsHash": "QmZUBx6N8aMkCU2KSYHNXueLUQxfxFNR8uvwEkLahpsXb2",
        "PinSize": 58424,
        "Timestamp": "2021-11-30T00:22:11.730Z",
    },
    {
        "IpfsHash": "QmeEGzEGbBjpnWTCS7o8y2bgaTdgthvFEHAER4mzX9bQEJ",
        "PinSize": 57346,
        "Timestamp": "2021-11-30T00:22:12.475Z",
    },
    {
        "IpfsHash": "QmdSDGpGDx6MDSDKxfWkhTUSnbjn2JQWoKDTxc4uaBCH8M",
        "PinSize": 57623,
        "Timestamp": "2021-11-30T00:22:13.143Z",
    },
    {
        "IpfsHash": "QmRUZgzuCg4F2hCCWnoXCAHtyRkRcymUWeHEAYLQ6wBMYT",
        "PinSize": 58155,
        "Timestamp": "2021-11-30T00:22:13.765Z",
    },
    {
        "IpfsHash": "QmNofJBHX8LpBjnB35FKkfEJkMHebSNkeRiHUSJX8TFzwt",
        "PinSize": 56609,
        "Timestamp": "2021-11-30T00:22:14.472Z",
    },
    {
        "IpfsHash": "QmTYbnxUii8HFRyRAyvBrEKWaKMdV6HehdDiug357y1W3g",
        "PinSize": 49389,
        "Timestamp": "2021-11-30T00:22:15.118Z",
    },
    {
        "IpfsHash": "QmWSzUz5uhs18skNgzRrwZ3Dsx53fE3g4whBfm1Grs9pwe",
        "PinSize": 55956,
        "Timestamp": "2021-11-30T00:22:15.737Z",
    },
    {
        "IpfsHash": "QmP1HtivqjDaRdZC2wWa24AqNDboVoeV4cnWHP6CLfyajz",
        "PinSize": 58858,
        "Timestamp": "2021-11-30T00:22:16.356Z",
    },
    {
        "IpfsHash": "QmVR7hosBX71j5REFeqPMVSXzmdFj1iMYoFakHSB1wmHec",
        "PinSize": 58173,
        "Timestamp": "2021-11-30T00:22:16.872Z",
    },
    {
        "IpfsHash": "QmQtqxUL5VF2YDVm2i79vEpBiHjAELzjL9dFA2UDP8AkFJ",
        "PinSize": 49496,
        "Timestamp": "2021-11-30T00:22:17.510Z",
    },
    {
        "IpfsHash": "QmTe1CcAzhhDWNVXHSECAEVAfbVEgvxyZAuqHbWAG14Emr",
        "PinSize": 48664,
        "Timestamp": "2021-11-30T00:22:18.171Z",
    },
]

metadata = []


counter = 0
for i in hashTable:
    hash = i["IpfsHash"]
    name = f"squirrel{counter}"
    imageuri = f"ipfs://{hash}"
    meta = {
        "name": name,
        "hash": hash,
        "imageuri": imageuri,
    }
    metadata.append(meta)
    counter += 1

with open("./assets/imageuri.json", "w") as file:
    json.dump(metadata, file)
