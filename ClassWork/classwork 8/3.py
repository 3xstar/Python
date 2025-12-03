# Написание функции# для нахождения максимального общего делителя
# неограниченного набора целых чисел
def func(*parameters):
    a = max(parameters)
    b = []
    for i in range(1, a + 1):
        g = True
        for k in parameters:
            if k % i != 0:
                g = False
        if g == True:
            b.append(i)
    print(b)
    print("Минимальный общий делитель будет равен: ", min(b))
    print("Максимальный общий делитель будет равен: ", max(b))
func(12, 60)