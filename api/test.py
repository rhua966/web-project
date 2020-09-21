import requests

BASE_URL = "http://127.0.0.1:5000/"

data = [
    {"likes": 10, "name": "Tim", "views": 5003123210},
    {"likes": 10, "name": "Kyle", "views": 821},
    {"likes": 10, "name": "Huang", "views": 2012},
    {"likes": 10, "name": "Lee", "views": 312}
]

for i in range(len(data)):
    response = requests.put(BASE_URL + f"video/{i}", data[i])
    print(response.json())

response = requests.delete(BASE_URL + "video/0")
print(response)

input()
response = requests.get(BASE_URL + "video/2")

print(response.json())