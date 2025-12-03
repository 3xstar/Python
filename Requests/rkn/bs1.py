import requests
import bs4

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Accept": "application/json",
}
response = requests.get("https://rkn.gov.ru/", headers=headers)

print(response.text)

with open("rkn.html", "w+", encoding="utf-8") as file:
    file.write(response.text)