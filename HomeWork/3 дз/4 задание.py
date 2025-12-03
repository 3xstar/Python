# 4 задание
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
if a == b:
    print("Числа равны")
elif a > b or b > a:
    if a > b:
        print(b, a)
    if b > a:
        print(a, b)
