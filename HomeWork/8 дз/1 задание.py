import random
numbers = []
numbers2 = []
for i in range(10):
    numbers.append(random.randint(-10, 10))
    numbers2.append(random.randint(-10, 10))
print("Сгенерированные списки: ", numbers, numbers2)
print("a = Сформировать третий список, содержащий элементы обоих списков")
print("b = Сформировать третий список, содержащий элементы обоих списков без повторений")
print("c = Сформировать третий список, содержащий элементы общие для двух списков")
print("d = Сформировать третий список, содержащий только уникальные элементы каждого из списков")
print("e = Сформировать третий список, содержащий только минимальное и максимальное значение каждого из списков")
list = input("Какой список желаете создать? (от a до e): ")

if list == "a":
    numbers3 = []
    numbers3.extend(numbers)
    numbers3.extend(numbers2)
    print("Общий список: ", numbers3)

if list == "b":
    numbers4 = numbers + numbers2
    for i in numbers4:
        a = numbers4.count(i)
        while a > 1:
            numbers4.remove(i)
            a -= 1
    print("Общий список без повторений: ", numbers4)

if list == "c":
    numbers5 = numbers + numbers2
    for i in numbers5:
        if i in numbers and i not in numbers2:
            numbers5.remove(i)
        if i in numbers2 and i not in numbers:
            numbers5.remove(i)
    print("Список с общими элементами: ", numbers5)

if list == "d":
    numbers6 = numbers + numbers2
    for i in numbers6:
        if i in numbers and i in numbers2:
            numbers6.remove(i)
    print("Уникальные элементы из списков: ", numbers6)


if list == "e":
    a = [min(numbers), max(numbers), min(numbers2), max(numbers2)]
    print("Минимум и максимум из первого и второго списка: ", a)


