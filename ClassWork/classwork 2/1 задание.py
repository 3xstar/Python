number = int(input("Введите число: "))
x = 1
while x < 10:
    print(number, "*", x, "=", number * x, end="    ")
    x += 1