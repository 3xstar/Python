try:
    a = []
    numb = int(input("Введите число для добавления в список: "))
    a.append(numb)
    numb = int(input("Введите число для добавления в список: "))
    a.append(numb)
    c = input("Если хотите закончить список, напишите exit: ")
    while c != "exit":
        numb = int(input("Введите число для добавления в список: "))
        a.append(numb)
        numb = int(input("Введите число для добавления в список: "))
        a.append(numb)
        c = input("Если хотите закончить список, напишите exit: ")
    else:
        print("Получившийся список: ", a)
except ValueError:
    b = input("Вы ввели не число, попробовать снова? (да или нет): ")
    if b == "да":
        a = []
        numb = int(input("Введите число для добавления в список: "))
        a.append(numb)
        numb = int(input("Введите число для добавления в список: "))
        a.append(numb)
        c = input("Если хотите закончить список, напишите exit: ")
        while c != "exit":
            numb = int(input("Введите число для добавления в список: "))
            a.append(numb)
            numb = int(input("Введите число для добавления в список: "))
            a.append(numb)
            c = input("Если хотите закончить список, напишите exit: ")
        else:
            print("Получившийся список: ", a)
    if b == "нет":
        print("Программа завершена")