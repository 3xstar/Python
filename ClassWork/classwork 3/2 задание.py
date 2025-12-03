summa = 0
k = int(input("Введите число: "))
for i in range(1, k):
    if i % 2 != 0:
        summa += i**2
print(summa)