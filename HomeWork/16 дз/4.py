# Создайте программу «Книжная коллекция». Нужно
# хранить информацию о книгах: автор, название книги,
# жанр, год выпуска, количество страниц, издательство.
# Требуется реализовать возможность добавления, удаления, поиска, замены данных. Используйте словарь для
# хранения информации.
book_info = {1: ["Автор: Джек Лондон", "Название: Белый клык", "Жанр: реализм", "Год выпуска: 1906", "Количество страниц: 200", "Издательство: Macmillan Company"]}
print("Список информации о книгах:", book_info)
while True:
    try:
        def action_menu():
            print("\n1. Добавить книгу"
                  "\n2. Удалить книгу"
                  "\n3. Поиск книги"
                  "\n4. Замена данных книги")
            action = int(input("\nВведите номер действия: "))
            match action:
                case 1:
                    new_book = []
                    author = input("\nВведите автора книги: ")
                    new_book.append(f"Автор: {author}")
                    book_name = input("Введите название книги: ")
                    new_book.append(f"Название: {book_name}")
                    genre = input("Введите жанр книги: ")
                    new_book.append(f"Жанр: {genre}")
                    start_year = int(input("Введите год выпуска книги: "))
                    new_book.append(f"Год выпуска: {start_year}")
                    list_count = int(input("Введите количество страниц книги: "))
                    new_book.append(f"Количество страниц: {list_count}")
                    publisher = input(f"Введите издательство книги: ")
                    new_book.append(f"Издательство: {publisher}")
                    book_list = list(book_info)
                    book_info[len(book_list) + 1] = new_book
                    print(f"\nНовая книга добавлена")
                    print("Список книг:", book_info)


                case 2:
                    index = int(input("\nВведите номер книги для удаления: "))
                    for key, value in list(book_info.items()):
                        if index == key:
                            del book_info[key]
                    print("\nКнига удалена")
                    print("Список книг:", book_info)

                case 3:
                    int_index = int(input("\nВведите порядковый номер книги: "))
                    for key, value in book_info.items():
                        if int_index == key:
                            print("\nКнига под этим номером: ", value)

                case 4:
                    int_index = int(input("\nВведите номер книги для замены данных: "))
                    for key, value in list(book_info.items()):
                        if int_index == key:
                            new_book = []
                            author = input("\nВведите автора книги: ")
                            new_book.append(f"Автор: {author}")
                            book_name = input("Введите название книги: ")
                            new_book.append(f"Название: {book_name}")
                            genre = input("Введите жанр книги: ")
                            new_book.append(f"Жанр: {genre}")
                            start_year = int(input("Введите год выпуска книги: "))
                            new_book.append(f"Год выпуска: {start_year}")
                            list_count = int(input("Введите количество страниц книги: "))
                            new_book.append(f"Количество страниц: {list_count}")
                            publisher = input(f"Введите издательство книги: ")
                            new_book.append(f"Издательство: {publisher}")
                            book_list = list(book_info)
                            book_info[key] = new_book
                            print(f"\nНовая книга добавлена")
                            print("Список книг:", book_info)
        action_menu()
    except Exception:
        print("В программе произошла ошибка, попробуйте снова")