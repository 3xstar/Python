# Создайте программу «Англо-французский словарь».
# Нужно хранить слово на английском языке и его перевод
# на французский. Требуется реализовать возможность добавления, удаления, поиска, замены данных. Используйте
# словарь для хранения информации.
words = {1: "Food = Nourriture", 2: "Life = Vie", 3: "Love = Amour", 4: "Human = Humain", 5: "Death = Mort"}
print("Список слов:", words)
while True:
    try:
        def action_menu():
            print("\n1. Добавить слово"
                  "\n2. Удалить слово"
                  "\n3. Поиск слова"
                  "\n4. Замена данных слова")
            action = int(input("\nВведите номер действия: "))
            match action:
                case 1:
                    new_word = []
                    english = input("\nВведите слово на английском: ")
                    new_word.append(english)
                    french = input("Введите это же слово на французском: ")
                    new_word.append(french)
                    words_list = list(words)
                    words[len(words_list) + 1] = f"{new_word[0]} = {new_word[1]}"
                    print(f"\nНовое слово: {words[len(words_list) + 1]}, добавлено")
                    print("Список слов:", words)

                case 2:
                    index = int(input("\nВведите номер слова для удаления: "))
                    for key, value in list(words.items()):
                        if index == key:
                            del words[key]
                    print("\nСлово удалено")
                    print("Список слов:", words)

                case 3:
                    int_index = int(input("\nВведите порядковый номер слова: "))
                    for key, value in words.items():
                        if int_index == key:
                            print("\nСлово под этим номером: ", value)

                case 4:
                    int_index = int(input("\nВведите номер слова для замены данных: "))
                    for key, value in list(words.items()):
                        if int_index == key:
                            new_word = []
                            english = input("\nВведите новое слово на английском: ")
                            new_word.append(english)
                            french = input("Введите это же слово на французском: ")
                            new_word.append(french)
                            words_list = list(words)
                            words[key] = f"{new_word[0]} = {new_word[1]}"
                            print(f"\nОбновленное слово: {words[key]}")
                            print("Список слов:", words)
        action_menu()
    except Exception:
        print("В программе произошла ошибка, попробуйте снова")