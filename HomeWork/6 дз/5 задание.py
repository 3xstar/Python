a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))

if b > a:
    for i in range(a, b):
        if i % 2 != 0:
            print(i)
if a > b:
    a, b = b, a
    for i in range(a, b):
        if i % 2 != 0:
            print(i)
