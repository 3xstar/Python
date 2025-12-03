try: 
    import random
    list = [i*0 + random.randint(1,10) for i in range(5)]
    print("Исходный список: ", list)
    print("Отсортированный список: ", sorted(list))
except SyntaxError:
        print("В списке есть некорректные значения")
    