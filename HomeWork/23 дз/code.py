import requests
from deep_translator import GoogleTranslator
import json

api_key="8110d1f7a0898085a1cb3eea93b1c223"
city = input("Введите название города для вычисления погоды: ")

response = requests.get(f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}")

if response.status_code==200:
    data = response.json()

    temperature = data["list"][0]["main"]["temp"]
    humidity = data["list"][0]["main"]["humidity"]
    description = data["list"][0]["weather"][0]["description"]
    print(f"Выбранный город: {city}")
    print("Температура:",temperature)
    print("Влажность:",humidity)
    print("Описание:", GoogleTranslator(source="en", target="ru").translate(description))


def kelvin_to_c(i):
    temperature_in_c = i - 273.15
    return temperature_in_c

print("Температура в цельсиях:",kelvin_to_c(temperature))


with open("openweather.json", "w+", encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=4)


def forecast_for_5_days():
    print("Прогноз на следующие 5 дней:")
    for i in range(0,5):
        days = data["list"][i * 8]
        temp = kelvin_to_c(i=days["main"]["temp"])
        hum = days["main"]["humidity"]
        desc = GoogleTranslator(source="en", target="ru").translate(days["weather"][0]["description"])
        print("Температура:", temp, "Влажность:", hum, "Описание погоды:", desc)
forecast_for_5_days()