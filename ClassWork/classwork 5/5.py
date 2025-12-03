try:
    import random
    list = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    list2 = [random.choice(list), random.choice(list), random.choice(list), random.choice(list), random.choice(list)]
    print(list2)
    a = input("Выберите букву для удаления: ")
    list2.remove(a)
    print(list2)
except ValueError:
    print("В списке нет данной буквы")