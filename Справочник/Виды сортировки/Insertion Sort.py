import random
nums = [random.randint(1,10) for _ in range(random.randint(5, 10))]
print("Исходный список:", nums)

def insertion(nums_list):
    length = len(nums_list)
    for i in range(1, length):
        n = nums_list[i]
        j = i

        while j > 0 and nums_list[j - 1] > n:
            nums_list[j] = nums_list[j - 1]
            j -= 1

        nums_list[j] = n
    return nums_list

print("Отсортированный список: ",insertion(nums))