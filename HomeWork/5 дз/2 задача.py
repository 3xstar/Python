number = int(input("Введите число для вычисления факториала: "))
fact = 1

while number > 1:
    fact *= number
    number -= 1

print("Факториал данного числа: ", fact)
