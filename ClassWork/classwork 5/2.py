try:
    import random
    a = int(input("Введите делитель: "))
    list = [i*0 + random.randint(1,10) for i in range(5)]
    print("Исходный список: ", list)
    for i in list:
        i /= a
        print("Результат деления: ", i)
except ZeroDivisionError:
    print("На нуль делить нельзя")