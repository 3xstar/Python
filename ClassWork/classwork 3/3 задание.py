n = int(input("Введите число: "))
if n > 100:
    for i in range(1, n):
        if i**3 < n:
            print(i)
