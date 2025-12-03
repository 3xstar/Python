import requests
import json

username = input("Введите имя пользователя: ")

response = requests.get(f"https://api.github.com/users/{username}/repos")

if response.status_code == 200:
    data = response.json()

    with open("github.json", "w+", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

    print("Список публичных репозиториев пользователя: ")

    for i in range(0, len(data)):
        print(data[i]["name"])