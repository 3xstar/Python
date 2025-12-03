# Входные данные
# В первой строке входного файла INPUT.TXT записано целое
# число N (0 < N ≤ 100). Во второй строке через пробел заданы
# N натуральных чисел, не превосходящих 100, соответствующие
# стоимости C[i] 1 сантиметра волос за каждый i-й день.
#
# Выходные данные
# В единственную строку выходного файла OUTPUT.TXT нужно вывести
# максимальную денежную сумму, которую может заработать неформал за N дней.
import random
dni = random.randint(1, 10)
stoimost = [random.randint (1, 100) + i * 0 for i in range(dni)]
print(dni)
print(stoimost)
# def summa_volosni(dni, stoimost):
#     sum = 0
#     for i in stoimost:
#         sum += i
#     return(sum)
# print(summa_volosni(dni, stoimost))
def summa_volosni(dni, stoimost):
    a = max(stoimost)
    day_with_max = stoimost.index(a)
    sum = 0
    length_volos = 0
    for i in range(dni):
        length_volos += 1
        if i == day_with_max:
            sum += a * length_volos
            length_volos = 0
            a = max(stoimost)
            day_with_max = stoimost.index(a)
    return sum
print(summa_volosni(dni,stoimost))