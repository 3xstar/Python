# 1 Напишите функцию unique_words_count(text), которая принимает строку text
# и возвращает количество уникальных слов в этой строке.
# Считайте, что слова разделяются пробелами,
# а знаки препинания должны игнорироваться (используйте регулярные выражения или методы строк для удаления знаков препинания).
def unique_words_count(text = input("Введите текст: ")):
    text = text.split()
    unique_list = []
    for i in text:
        if text.count(i) == 1:
            unique_list.append(i)
    print("Уникальные слова из данного текста: ", *unique_list, sep=" ")
unique_words_count()

