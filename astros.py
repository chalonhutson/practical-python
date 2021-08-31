import requests

response = requests.get("http://api.open-notify.org/astros.json")
json = response.json()


print("The people currently in space are: ")

for i in json["people"]:
    print(i["name"])