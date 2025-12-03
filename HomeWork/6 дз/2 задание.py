a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))

if a > b:
    for i in range(b, a):
        if i % 2 != 0:
            print(i)
if b > a:
    for i in range(a, b):
        if i % 2 != 0:
            print(i)
