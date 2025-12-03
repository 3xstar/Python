from re import search

import bs4

with open("rkn.html", "r", encoding="utf-8") as file:
    src = file.read()

soup = bs4.BeautifulSoup(src, "lxml")

title = soup.title
# print(title)
print(title.text)

#find - поиск первого тега
#find_all - поиск всех тегов

# page_h2 = soup.find("h2")
# print(page_h2)
# print(page_h2.text)
#
# page_p = soup.find("p")
# print(page_p)
#
# page_all_h3 = soup.find_all("h3")
# print(page_all_h3)
#
# for item in page_all_h3:
#     print(item.text)

contact_info = soup.find_all("div", class_="contacts-info-card-element-about")
# print(contact_info)

for item in contact_info:
    adress = item.find_all("p", class_="contacts-info-card-element-about-preview")
    for adress_item in adress:
        print(adress_item.text)

search_param = {"class": "activities-card-element-footer-number"}
result = soup.find_all("p", search_param)
# print(result)

search_param = {"class": "activities-card-element-footer-preview"}
result_preview = soup.find_all("p", search_param)
# print(result_preview)

for i in range(len(result)):
    print(result[i].text, result_preview[i].text.strip())

    