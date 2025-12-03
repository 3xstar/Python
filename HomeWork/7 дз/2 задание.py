a = int(input("Введите первое число (начало диапозона): "))
b = int(input("Введите второе число (конец диапозона): "))
if a < b:
    for i in range(a, b):
        print("Числа в указанном диапозоне: ",i)
    for i in range(a, b):
        print("Числа диапозона в убывающем порядке: ",a - i + b)
    for i in range(a, b):
        if i % 7 == 0:
            print("Числа кратные 7: ",i)
    for i in range(a, b):
        if i % 5 == 0:
            print("Числа кратные 5: ",i)
elif a == b:
    print("Вы ввели равные числа")
else:
    print("Начало диапозона не может быть больше конца")