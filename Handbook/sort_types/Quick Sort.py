import random

def quick_sort(list):
    if len(list) <= 1:
        return list

    mid_element = list[len(list) // 2]

    less_element = [x for x in list if x < mid_element]
    equal_elements = [x for x in list if x == mid_element]
    grater_elements = [x for x in list if x > mid_element]

    return quick_sort(less_element) + equal_elements + quick_sort(grater_elements)

list_example = [random.randint(5, 10) for _ in range(random.randint(10, 100))]

print("Неотсортированный список: ", list_example)
print("Отсортированный список: ", quick_sort(list_example))