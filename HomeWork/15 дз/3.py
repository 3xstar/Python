str_list = ["Pirozok", "Oguzki", "Abdul", "Uzbek", "Tatar"]

n = len(str_list)
for i in range(1, n):
    item_to_insert = str_list[i]
    j = i - 1

    while j >= 0 and str_list[j] > item_to_insert:
        str_list[j + 1] = str_list[j]
        j -= 1

    str_list[j + 1] = item_to_insert

print(str_list)
