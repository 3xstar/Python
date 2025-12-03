import random

class Human:
    def __init__(self, name, date, number, town, country, address):
        self._name = name
        self._date = date
        self._number = number
        self._town = town
        self._country = country
        self._address = address

    def show_info(self):
        print(f"Имя: {self._name}",f"Дата рождения:  {self._date}",f"Номер телефона: {self._number}",f"Город: {self._town}",f"Страна: {self._country}",f"Домашний адрес: {self._address}")

    def change_number(self):
        new_number = int(input("Введите новый номер: "))
        self._number = new_number
        print("Номер телефона изменен")

    def change_address(self):
        new_country = input("Введите новую страну: ")
        new_town = input("Введите новый город: ")
        new_address = input("Введите новый адрес: ")

        self._country = new_country
        print("Страна изменена")
        self._town = new_town
        print("Город изменен")
        self._address = new_address
        print("Адрес изменен")
users = []

names = ["Дима", "Захар", "Гриша", "Галя", "Вадим"]
cities = ["Chitago", "PythonStan", "RPOcity", "Saint-Vegas"]
countries = ["Niggeria", "Russia", "India", "Probirka", "ChinaStan"]
streets = ["Kolotuskino" "Skverovo", "Marka", "Pedro", "С++"]

def generate_humans(count, users):
    for i in range(count):
        name = random.choice(names)
        city = random.choice(cities)
        number = random.randint(10000000000, 99999999999)
        country = random.choice(countries)
        address = f"{random.choice(streets)} {random.randint(1,100)}"
        date = (f"{random.randint(1, 30)}."
                f"{random.randint(1,12)}."
                f"{random.randint(1950, 2015)}")
        human = Human(name, date, number, city, country, address)
        users.append(human)
    return users

users = generate_humans(100, users)

for user in users:
    user.show_info()

