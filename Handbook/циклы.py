# a = 0
# while a < 10:
#     print(a)
#     a += 1 #прибавить к переменной 1
#
# a = 10
# while a > 10:
#     print(a)
#     a -= 1

# a = int(input("Введите первое число: "))
# b = int(input("Введите второе число: "))
# if a < b:
#     while a < b:
#         print(a)
#         a += 1
# if a > b:
#     while a > b:
#         print(b)
#         b += 1

# a = int(input("Введите первое число: "))
# b = int(input("Введите второе число: "))
# if a < b:
#     while a < b:
#         if a % 2 != 0:
#             print(a)
#         a += 1
# if a > b:
#     while a > b:
#         if b % 2 != 0:
#             print(b)
#         b += 1

# a = int(input("Введите первое число: "))
# b = int(input("Введите второе число: "))
# if a < b:
#     while a < b:
#         if a % 2 != 0:
#             print(a)
#         a += 1
# if a > b:
#     while a > b:
#         if b % 2 != 0:
#             print(b)
#         b += 1

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
if a > b:
    a, b = b, a
if a < b:
    while a < b:
        if a % 2 != 0:
            print(a)
        a += 1



