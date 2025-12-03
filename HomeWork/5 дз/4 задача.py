dlina = int(input("Введите длину линии: "))
symbol = input("Введите желаемый символ: ")

if dlina > 0 and len(symbol) == 1:
    print(dlina * symbol)

elif len(symbol) >= 2:
    print("Вы ввели больше одного символа")

elif dlina <= 0:
    print("Вы ввели нулевое или отрицательное число")