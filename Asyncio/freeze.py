import random

def random_number(count):
    for i in range(count):
        print("заморозка")
        yield  i
        print("разморозка")

print(random_number)

number = random_number(10) #Создание генератора
print(number)

print(next(number)) #Попросить генератор выдать число
print(next(number))
print(next(number))
print(next(number))