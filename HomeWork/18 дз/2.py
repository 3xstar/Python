class Car:
    def __init__(self, wheels, engine, doors):
        self.wheels = wheels
        self.engine = engine
        self.doors = doors

class Wheels(Car):
    def __init__(self, wheels, engine, doors):
        super().__init__(wheels, engine, doors)

    def wheel_input(self):
        self.wheels = input("Введите тип колес автомобиля: ")


class Engine(Car):
    def __init__(self, wheels, engine, doors):
        super().__init__(wheels, engine, doors)

    def engine_input(self):
        self.engine = input("Введите мощность двигателя автомобиля: ")


class Doors(Car):
    def __init__(self, wheels, engine, doors):
        super().__init__(wheels, engine, doors)

    def door_input(self):
        self.doors = input("Введите размер дверей автомобиля: ")

wheel = Wheels("", "", "")
wheel.wheel_input()
engine_power = Engine("", "", "")
engine_power.engine_input()
door = Doors("", "", "")
door.door_input()
car = Car(wheel, engine_power, door)
print(f"У моей машины {wheel} колёса, мощность двигателя составляет {engine_power}, двери {door} размера")

