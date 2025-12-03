str_list = ["Лишь одно в моем кармане", "Беспонтовый пирожок",
            "Каждый из нас беспонтовый пирожок...", "Туту туруруруру тутуру",
            "@Гражданская оборона"]

n = len(str_list)
for i in range(n):
    min_index = i

    for j in range(i + 1, n):
        if len(str_list[j]) < len(str_list[min_index]):
            min_index = j

    str_list[i], str_list[min_index] = str_list[min_index], str_list[i]

print(str_list)
