import random
random_list = [random.randint(1,10) for _ in range(random.randint(5,10))]
print("Исходный список: ", *random_list)
length = len(random_list)
sorted_list = []
operation_count = 0

for i in range(length):
    min_element = random_list[0]

    for element in random_list:
        if min_element > element:
            min_element = element
        operation_count += 1

    sorted_list.append(min_element)
    random_list.remove(min_element)

print("Отсортированный список: ", *sorted_list)
print("Количество операций: ", operation_count)