class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def info(self):
        print(f"Название: {self.title}, автор: {self.author}, год: {self.year}")


class Library:
    def __init__(self, book_list):
        self.book_list = book_list

    def __len__(self, book_list):
        return len(book_list)

    def add_book(self, book, book_list):
        book_list.append(book)
        print(f"Книга {book.title} добавлена")
        return book_list

    def delete_book(self, book, book_list):
        book_list.remove(book)
        print(f"Книга {book.title} удалена")
        return book_list

    def print_books(self, book_list):
        print("Список книг в библиотеке:")
        for i in book_list:
            i.info()

b_l = []
b1 = Book("МГЕ братики", "Снайпер", "1488")
library = Library(b_l)

library.add_book(b1, b_l)
library.print_books(b_l)
library.delete_book(b1, b_l)


