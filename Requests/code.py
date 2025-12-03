import requests

response = requests.get("https://unity.com/")
print(response.status_code)
print(response.content)
print(response.headers)

with open("list.html", "w+", encoding="utf-8") as file:
    file.write(response.text)