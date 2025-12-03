import requests

API_KEY = "db407942e0cd49b1ac8506c49199462b"  # Замените на реальный ключ
ENDPOINT = "https://api.spoonacular.com/recipes/complexSearch"

params = {
    "apiKey": API_KEY,
    "query": "pasta",
    "number": 1
}

try:
    # Указываем таймаут (секунды на подключение и чтение)
    response = requests.get(ENDPOINT, params=params, timeout=(5, 10))
    response.raise_for_status()  # Проверка на HTTP-ошибки (4xx, 5xx)

    if response.status_code == 200:
        print("API работает! Ответ:")
        print(response.json())
    else:
        print(f"Ошибка API: {response.status_code}")
        print(response.text)

except requests.exceptions.Timeout:
    print("Ошибка: Таймаут при подключении к Spoonacular API. Проверьте интернет или попробуйте позже.")
except requests.exceptions.RequestException as e:
    print(f"Ошибка запроса: {e}")
except Exception as e:
    print(f"Неизвестная ошибка: {e}")