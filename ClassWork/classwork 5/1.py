try:
    import random
    a = 0
    list = [i*0 + random.randint(1,10) for i in range(5)]
    for i in list:
        a += i
    print("Исходный список: ", list)
    print("Сумма чисел: ", a)
except ValueError:
    print("В листе есть буквы")