# Реализуйте класс «Автомобиль». Необходимо хранить
# в полях класса: название модели, год выпуска, производителя, объем двигателя, цвет машины, цену. Реализуйте
# методы класса для ввода данных, вывода данных, реализуйте доступ к отдельным полям через методы класса.

class Car:
    def __init__(self, name, year, manufacturer, engine, color, price):
        self.name = name
        self.year = year
        self.manufacturer = manufacturer
        self.engine = engine
        self.color = color
        self.price = price

    def input(self):
        self.name = input("Введите название модели машины: ")
        self.year = int(input("Введите год выпуска машины (в цифрах): "))
        self.manufacturer = input("Введите название производителя машины: ")
        self.engine = int(input("Введите объём двигателя машины (в цифрах): "))
        self.color = input("Введите цвет машины: ")
        self.price = int(input("Введите цену машины (в цифрах): "))

    def conclusion(self):
        print(f"\nНазвание машины: {self.name}")
        print(f"Год выпуска машины: {self.year}")
        print(f"Производитель машины: {self.manufacturer}")
        print(f"Объём двигателя машины: {self.engine}")
        print(f"Цвет машины: {self.color}")
        print(f"Цена машины: {self.price}")

    def name(self):
        return self.name

    def year(self, year):
        return self.year

    def manufacturer(self):
        return self.manufacturer

    def engine(self):
        return self.engine

    def color(self):
        return self.color

    def price(self):
        return self.price

car_info = Car("", 0, "", 0, "", 0)
car_info.input()
car_info.conclusion()
engine_info = car_info.engine
print("\nОбъём двигателя машины: ", engine_info)