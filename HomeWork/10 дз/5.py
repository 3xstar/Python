def check_int(help = "Введите число: "):
    while True:
        try:
            a = input(help)
            a = int(a)
            return (a)
        except ValueError:
            print("Вы ввели не число, попробуйте снова")
def normalize(a, b):
    if a > b:
        a, b = b, a
    return(a, b)
a = check_int("Введите первое число: ")
b = check_int("Введите второе число: ")
a, b = normalize(a, b)
def result():
    proizvedenie = 1
    for i in range(a, b + 1):
        proizvedenie *= i
    print("Произведение в диапозоне данных чисел равно:",proizvedenie)
result()

