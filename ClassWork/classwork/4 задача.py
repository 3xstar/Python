a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
if a < b:
    print(a)
elif b < a:
    print(b)
else:
    print(b, "=", a)