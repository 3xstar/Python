class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    surname = "Попов"

std1 = Student("Захар", 17)
print(std1.surname) #Значение атрибута класса для всех экземпляров
print(std1.name) #Значение атрибута объекта уникально для каждого объекта