try:
    import random
    list = [i*0 + random.randint(1,10) for i in range(5)]
    print(list)
    a = int(input("Введите нужное число: "))
    for i in list:
        if a == i:
            print("Искомое число")
        else:
            print("Другое число")
except ValueError:
    print("Среди чисел есть буква, что привело к ошибке")