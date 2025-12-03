# Реализуйте класс «Книга». Необходимо хранить в
# полях класса: название книги, год выпуска, издателя,
# жанр, автора, цену. Реализуйте методы класса для ввода
# данных, вывода данных, реализуйте доступ к отдельным
# полям через методы класса.

class Book:
    def __init__(self, name, year, publisher, genre, author, price):
        self.name = name
        self.year = year
        self.publisher = publisher
        self.genre = genre
        self.author = author
        self.price = price

    def input(self):
        self.name = input("Введите название книги: ")
        self.year = int(input("Введите год выпуска книги (в цифрах): "))
        self.publisher = input("Введите название производителя книги: ")
        self.genre = input("Введите жанр книги: ")
        self.author = input("Введите имя Автора книги: ")
        self.price = int(input("Введите цену книги (в цифрах): "))

    def conclusion(self):
        print(f"\nНазвание книги: {self.name}")
        print(f"Год выпуска книги: {self.year}")
        print(f"Издатель книги: {self.publisher}")
        print(f"Жанр книги: {self.genre}")
        print(f"Автор книги: {self.author}")
        print(f"Цена книги: {self.price}")

    def name(self):
        return self.name

    def year(self, year):
        return self.year

    def publisher(self):
        return self.publisher

    def genre(self):
        return self.genre

    def author(self):
        return self.author

    def price(self):
        return self.price

book_info = Book("", 0, "", "", "", 0)
book_info.input()
book_info.conclusion()
genre_info = book_info.genre
print("\nЖанр книги: ", genre_info)