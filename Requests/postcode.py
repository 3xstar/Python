import requests

data = {"email": "lol@gmail.com"}
response = requests.post("https://httpbin.org/post", data=data)
print(response.content)