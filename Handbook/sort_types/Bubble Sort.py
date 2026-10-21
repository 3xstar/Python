import random
random_list = [random.randint(1,10) for _ in range(random.randint(5,10))]
print("Исходный список: ", *random_list)
length = len(random_list)
operation_count = 0

for i in range(length):

    for j in range(1, length - i):
        element_one = random_list[j - 1]
        element_two = random_list[j]

        if element_two < element_one:
            random_list[j], random_list[j - 1] = (
                random_list[j - 1], random_list[j])

        operation_count += 1

print("Отсортированный список: ", *random_list)
print("Количество операций: ", operation_count)