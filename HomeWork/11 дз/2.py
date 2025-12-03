# Напишите функцию pascals_triangle(n), которая принимает число n и возвращает список
# из n списков, представляющих собой первые n строк треугольника Паскаля.
# В треугольнике Паскаля каждый элемент является суммой двух элементов, расположенных над ним.
def pascals_triangle(n = int(input("Введите количество списков: "))):
    list = []
    for i in range(0, n):
        row = [1] * (i + 1)
        for e in range(i + 1):
            if e != 0 and e != i:
                row[e] = list[i-1][e-1] + list[i - 1][e]
        list.append(row)
    for result in list:
        print(result)
pascals_triangle()
