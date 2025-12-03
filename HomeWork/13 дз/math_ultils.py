# Факториал
def fact(n = int(input("Введите число: "))):
    factor = 1
    for i in range(1, n + 1):
        factor *= i
    print("Факториал числа: ", factor)
fact()

# Число Фибоначчи
def fib(n = int(input("Введите число: ")), n1=0, n2=1):
    while n != 0:
        n1, n2 = n2, n1 + n2
        n -= 1
        if n > 0:
            n1, n2 = n2, n1 + n2
            n -= 1
    else:
        print("Число Фибоначчи: ", n1)
fib()

# Сумма
def summ(n = int(input("Введите число: "))):
    sum_result = 0
    number = str(n)
    if len(number) != 1:
        for i in number:
            sum_result += int(i)
    print("Сумма цифр числа: ",sum_result)
summ()

