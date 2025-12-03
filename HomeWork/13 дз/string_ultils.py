# Палиндром
def palindrome(word = input("Введите строку: ")):
    if word == word[::-1]:
        print("Строка является палиндромом")
    else:
        print("Строка не является палиндромом")
palindrome()

# Анаграмма
def anagramm(word = input("Введите первую строку: "), word2 = input("Введите вторую строку: ")):
    list_word = list(word)
    list_word2 = list(word2)
    list_word.sort()
    list_word2.sort()
    if list_word == list_word2:
        print("Строки являются анаграммами друг друга")
    else:
        print("Строки не являются анаграммами друг друга")
anagramm()

# Обратная строка
def reverse_word(word = input("Введите строку: ")):
    print(word[::-1])
reverse_word()
