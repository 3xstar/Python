a = int(input("Введите первое число (начало диапозона): "))
b = int(input("Введите второе число (конец диапозона): "))
if a < b:
    for i in range(a, b):
        if i % 3 == 0 and i % 5 != 0:
            print("Fizz")
        elif i % 5 == 0 and i % 3 != 0:
            print("Buzz")
        elif i % 3 == 0 and i % 5 == 0:
            print("Fizz Buzz")
        else:
            print(i)
elif a == b:
    print("Вы ввели равные числа")
else:
    print("Начало диапозона не может быть больше конца")