def print_text():
    with open("text.txt", "r+", encoding="utf-8") as file:
        text = file.read()

    print("Содержимое файла: ")
    print(text)

# print_text()

def text_count_words():
    with open("text.txt", "r+", encoding="utf-8") as file:
        text = file.read()
    words = text.split()
    print("Количество слов в тексте: ", len(words))

text_count_words()

def text_str():
    with open("text.txt", "r+", encoding="utf-8") as file:
        text = file.readlines()
    print("Количество строк в тексте: ", len(text))
    print("Самая длинная строка в тексте: ", max(text, key=len))

text_str()