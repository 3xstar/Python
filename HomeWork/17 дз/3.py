# Реализуйте класс «Стадион». Необходимо хранить в
# полях класса: название стадиона, дату открытия, страну,
# город, вместимость. Реализуйте методы класса для ввода
# данных, вывода данных, реализуйте доступ к отдельным
# полям через методы класса.

class Stadium:
    def __init__(self, name, year, country, city, capacity):
        self.name = name
        self.year = year
        self.country = country
        self.city = city
        self.capacity = capacity

    def input(self):
        self.name = input("Введите название стадиона: ")
        self.year = int(input("Введите год открытия стадиона (в цифрах): "))
        self.country = input("Введите страну, в которой находится стадион: ")
        self.city = input("Введите город, в котором находится стадион: ")
        self.capacity = int(input("Введите вместимость стадиона (в количестве людей): "))

    def conclusion(self):
        print(f"\nНазвание стадиона: {self.name}")
        print(f"Год открытия стадиона: {self.year}")
        print(f"Страна, в которой находится стадион: {self.country}")
        print(f"Город, в котором находится стадион: {self.city}")
        print(f"Вместимость стадиона: {self.capacity}")

    def name(self):
        return self.name

    def year(self, year):
        return self.year

    def country(self):
        return self.country

    def city(self):
        return self.city

    def capacity(self):
        return self.capacity()

stadium_info = Stadium("", 0, "", "", 0)
stadium_info.input()
stadium_info.conclusion()
city_info = stadium_info.city
print("\nГород, в котором находится стадион: ", city_info)
