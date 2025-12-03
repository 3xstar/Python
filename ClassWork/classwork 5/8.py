try:
    import random
    list = [i*0 + random.randint(1,10) for i in range(10)]
    print(list)
    for i in list:
        if type(i) != float:
            print("Число целое")
except ValueError:
    a = input("Вы ввели не целое число, попробовать снова? (да или нет): ")
    if a == "да":
        list = [i * 0 + random.randint(1, 10) for i in range(10)]
        print(list)
        for i in list:
            if type(i) != float:
                print("Число целое")
    if a == "нет":
        print("Программа завершена")

