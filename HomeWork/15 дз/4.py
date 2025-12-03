# Напишите программу, которая принимает список чисел
# и сортирует его в порядке убывания с помощью пузырьковой сортировки.​
numbers = [10,9,8,7,6,5,4,3,2,1]
swapped = True
while swapped:
    swapped = False
    for i in range(0, len(numbers) - 1):
        if numbers[i] < numbers[i + 1]:
            numbers[i + 1], numbers[i] = numbers[i], numbers[i + 1]
            swapped = True
print(numbers)