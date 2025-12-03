import requests
import json

response = requests.get("https://www.cbr-xml-daily.ru/daily_json.js")
print(response.content)

data = response.json()
print(data)
print(type(data))

with open("valutes.json", "w+", encoding="utf-8") as file:
    json.dump(data, file, indent=4)

valutes = data["Valute"].keys()
print(valutes)

for valute in valutes:
    print(valute, "-", data["Valute"][valute]["Value"])