# 3 Создайте функцию text_analysis(text), которая принимает строку text и возвращает список с информацией о тексте:
# ⦁	количество слов в тексте,
# ⦁	количество предложений,
# ⦁	средняя длина слова,
# ⦁	среднее количество слов в предложении.
def unique_words_count(text = input("Введите текст: ")):
    try:
        a = text.split()
        b = 0
        b += len(a)
        print("Количество слов в тексте: ", b)
        c = 0
        c += text.count(".")
        c += text.count("!")
        c += text.count("?")
        print("Количество предложений в тексте: ", c)
        d = 0
        d += len(text) - text.count(".") - text.count("!") - text.count("?") - text.count(" ")
        average = d/b
        print("Средняя длина слова в тексте: ", average)
        average_offer = b/c
        print("Среднее количество слов в предложении: ", average_offer)
    except ZeroDivisionError:
        print("В тексте нет предложений или нужных для их разделения символов.")
unique_words_count()



