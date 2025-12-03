import requests
import bs4

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Accept": "application/json",
}
response = requests.get("https://rkn.gov.ru/", headers=headers)

soup = bs4.BeautifulSoup(response.text, "lxml")

search_param = {"class" : "activities-card-element-footer-number"}
result = soup.find_all("p", search_param)

search_param = {"class" : "activities-card-element-footer-preview"}
result_preview = soup.find_all("p", search_param)

for i in range(len(result)):
    print(result[i].text, result_preview[i].text.strip())
