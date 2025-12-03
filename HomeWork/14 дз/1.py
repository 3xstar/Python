# Необходимо отсортировать первые две трети
# списка в порядке возрастания, если среднее
# арифметическое всех элементов больше нуля;
# иначе — лишь первую треть. Остальную часть
# списка не сортировать, а расположить в
# обратном порядке.
numbers = [7,6,1,8,2,5,3,9,4]
numbers2_3 = int((len(numbers)/3) * 2)
numbers1_3 = int(len(numbers)/3)

if sum(numbers)/len(numbers) > 0:
    n = 1
    while n < numbers2_3:
        for i in range(0, numbers2_3 - 1):
            if numbers[i] > numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
        n += 1

    else:
        rev_numbers = numbers[::-1]
        index = 0
        for i in range(numbers2_3, len(numbers)):
            numbers[i] = rev_numbers[index]
            index += 1

else:
    n = 1
    while n < numbers1_3:
        for i in range(0, numbers1_3 - 1):
            if numbers[i] > numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
        n += 1
    else:
        rev_numbers = numbers[::-1]
        index = 0
        for i in range(numbers1_3, len(numbers)):
            numbers[i] = rev_numbers[index]
            index += 1

print(numbers)





