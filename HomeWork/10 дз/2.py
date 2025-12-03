# Первая версия:
# def numbers():
#     while True:
#         try:
#             a = int(input("Введите первое число: "))
#             b = int(input("Введите второе число: "))
#             print("Четные числа в этом диапозоне: ")
#             if b > a:
#                 for i in range(a, b):
#                     if i % 2 == 0:
#                         print(i, end=" ")
#                 break
#             if a > b:
#                 a, b = b, a
#                 for i in range(a, b):
#                     if i % 2 == 0:
#                         print(i, end=" ")
#                 break
#         except ValueError:
#             print("Вы ввели не число, попробуйте снова")
# numbers()

# Вторая версия
def normalize(a, b):
    if a > b:
        a, b = b, a
    return(a, b)
def check_int(help = "Введите число: "):
    while True:
        try:
            a = input(help)
            a = int(a)
            break
        except ValueError:
            print("Вы ввели не число, попробуйте снова")
    return(a)
def result(a, b):
    a, b = normalize(a, b)
    print("Четные числа в этом диапозоне: ")
    for i in range(a, b + 1):
        if i % 2 == 0:
            print(i, end = " ")
a = check_int("Введите первое число: ")
b = check_int("Введите второе число: ")
result(a, b)






