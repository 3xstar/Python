import requests
import argparse

URL = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"
IAM_TOKEN = "AQVNxzmMWFQcyaMNwJlnh1Be_mLYZg0ZFBvHgs5u"
Folder_ID = "b1gfkj4il6umdgmv3729"

def run(iam_token, folder_id, user_text):
    # Собираем запрос
    data = {}
    # Указываем тип модели
    data["modelUri"] = f"gpt://{folder_id}/yandexgpt"
    # Настраиваем опции
    data["completionOptions"] = {"temperature": 1, "maxTokens": 1000}
    # Указываем контекст для модели
    data["messages"] = [
        {"role": "system", "text": "Ты маленький мальчик 5 лет, отвечай соответственно"},
        {"role": "user", "text": f"{user_text}"},
    ]

    # Отправляем запрос
    response = requests.post(
        URL,
        headers={
            "Accept": "application/json",
            "Authorization": f"Bearer {iam_token}"
        },
        json=data,
    ).json()

    # Распечатываем результат
    print(response["result"]["alternatives"][0]["message"]["text"])


if __name__ == '__main__':
    # parser = argparse.ArgumentParser()
    # parser.add_argument("--aje77665gl0sp6hgrg4p", required=True, help="IAM token")
    # parser.add_argument("--b1gfkj4il6umdgmv3729", required=True, help="Folder id")
    # parser.add_argument("--как заработать на машину", required=True, help="User text")
    # args = parser.parse_args()
    run("AQVNxzmMWFQcyaMNwJlnh1Be_mLYZg0ZFBvHgs5u", "b1gfkj4il6umdgmv3729", "как купить машину")