a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = input("Введите знак мат. операции: ")
if c == "+":
    print(a + b)
elif c == "-":
    print(a - b)
elif c == "!":
    print((a + b) / 2)
elif c == "*":
    print(a * b)
else:
    print("Такой операции нет")