summa = 0
count = 0
while True:
    a = input("Введите первое число: ")
    if a == "N":
        break
    count += 1
    summa += int(a)
print(summa/count)