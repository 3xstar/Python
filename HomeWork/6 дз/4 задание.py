a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))

if a > b:
    for i in range(b, a):
        print((a - i) + b)

if b > a:
    for i in range(a, b):
        print((b - i) + a)
