# Напишите программу, которая принимает список чисел
# и сортирует его в порядке убывания с помощью сортировки выбором.
numbers = [10,9,8,7,6,5,4,3,2,1]
for i in range(len(numbers)):
    lowest = i
    for j in range(i + 1, len(numbers)):
        if numbers[j] < numbers[lowest]:
            lowest = j
        numbers[j], numbers[lowest] = numbers[lowest], numbers[j]

print(numbers)