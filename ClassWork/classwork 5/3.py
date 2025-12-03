try:
    import random
    list = [i*0 + random.randint(1,10) for i in range(10)]
    print("Исходный список: ", list)
    print("Максимальное значение: ", max(list))
except IndexError:
    print("Список пуст, что привело к ошибке")