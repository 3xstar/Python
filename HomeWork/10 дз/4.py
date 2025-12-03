while True:
    try:
        while True:
            def numbers(help = "Введите число: "):
                a = input(help)
                a = int(a)
                return(a)
            a = numbers("Введите первое число: ")
            b = numbers("Введите второе число: ")
            c = numbers("Введите третье число: ")
            d = numbers("Введите четвертое число: ")
            e = numbers("Введите пятое число: ")
            def maxnumber(a, b, c, d, e):
                print("Максимальным значением из данных чисел является: ")
                m = max(a, b, c, d, e)
                print(m)
            maxnumber(a, b, c, d, e)
    except ValueError:
        print("Вы ввели не число, попробуйте снова")


