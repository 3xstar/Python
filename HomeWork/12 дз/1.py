# Рекурсивное разбиение Создайте функцию,
# которая рекурсивно разбивает целое число на
# все возможные комбинации меньших чисел,
# сумма которых равна исходному числу.
# Например, для числа 4 результатом могут быть
# [1, 1, 1, 1], [1, 1, 2], [2, 2], [1, 3] и т.д.
number = int(input("Введите число: "))
def number_rec(number, max_number = None):
    if number == 0:
        return [[]]
    if max_number is None:
        max_number = number

    rec_list = []

    for i in range(1, max_number + 1):
        if i <= number:
            for a in number_rec(number - i, i):
                rec_list.append([i] + a)
    return rec_list
result = number_rec(number)
for i in result:
    print(i)