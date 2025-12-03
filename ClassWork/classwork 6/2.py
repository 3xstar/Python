def normalize(a, b):
    if a > b:
        a, b = b,  a
    return(a, b)
def even_numbers(a, b):
    a, b = normalize(a, b)
    print("Не четные числа: ")
    for i in range(a, b):
            if i % 2 != 0:
                print(i, end = " ")
def input_int(help  =   "Введите число: "):
    while True:
        try:
            a   = input(help)
            a = int(a)
            break
        except ValueError:
            print("Вы ввели не число")
    return a
a = input_int("Введите первое число: ")
b = input_int("Введите второе число ")
even_numbers(a, b)
