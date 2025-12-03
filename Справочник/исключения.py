while True:
    try:
        a = int(input("Введите первое число: "))
        b = int(input("Введите второе число: "))
        print(a, "+", b, "=", a + b)
        print(a, "/", b, "=", a / b)
    except ValueError:
        print("Вы ввели буквы в числа")
    except ZeroDivisionError:
        print("Вы делите на ноль")
    except ArithmeticError:
        print("Ты математику незнаешь")
    else:
        print("Каким-то образом все работает")
    finally:
        print("Помни что, чтобы не случилось ты молодец!")