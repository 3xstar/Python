# Задание 2
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))
d = str(input("Введите операцию (максимум, минимум, среднее арифметическое): "))
if d == "максимум":
    if a > b and a > c:
        print(a)
    elif b > a and b > c:
    	print(b)
    elif c > a and c > b:
    	print(c)
    else: print("Вы ввели неверные данные.")
if d == "минимум":
    if a < b and a < c:
        print(a)
    elif b < a and b < c:
    	print(b)
    elif c < a and c < b:
    	print(c)
    else: print("Вы ввели неверные данные.")
if d == "среднее арифметическое":
    print((a + b + c) / 3)
