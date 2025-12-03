import sqlite3
import random

#1 ЗАДАНИЕ
booksDB = sqlite3.connect("books.db")
cursor = booksDB.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS books"
                "(id INTEGER"
                "title TEXT, "
                "author TEXT, "
                "year INTEGER, "
                "pages INTEGER)")

booksDB.close()


#2 ЗАДАНИЕ
def add_book(id, title, author, year, pages):
    booksDB = sqlite3.connect("books.db")
    cursor = booksDB.cursor()
    id = random.randint(000, 999)

    cursor.execute("INSERT INTO books (id, title, author, year, pages)"
                   "VALUES (?,?,?,?,?)", (id, title, author, year, pages))

    booksDB.commit()
    booksDB.close()

def show_books():
    booksDB = sqlite3.connect("books.db")
    cursor = booksDB.cursor()

    books = cursor.execute("SELECT * FROM books")
    print("Список книг:")
    for book in books:
        print(book)

# add_book(id, "Винипух", "Леброн Джеймс", 2007, 100)
# add_book(id, "Колобок", "Майкл Джордан", 2016, 200)
# add_book(id, "Три поросенка", "Кани Уэст", 2020, 300)
# add_book(id, "Бойцовский клуб", "Чак Паланик", 2000, 500)
# add_book(id, "Мертвые души", "Николай Гоголь", 1950, 700)
# show_books()


#3 ЗАДАНИЕ
def find_books_by_author(author):
    booksDB = sqlite3.connect("books.db")
    cursor = booksDB.cursor()

    cursor.execute("SELECT author FROM books")
    all_authors = cursor.fetchall()

    for one_author in all_authors:
        search_author = "".join(one_author)

        if search_author == author:
            books = cursor.execute("SELECT title from books WHERE author=?", (author,))
            print("Все книги с этим автором:")
            for book in books:
                print("".join(book))

# find_books_by_author("Майкл Джордан")

def update_page_count(book_id, new_pages):
    booksDB = sqlite3.connect("books.db")
    cursor = booksDB.cursor()

    cursor.execute("UPDATE books SET pages = ? WHERE id =?", (new_pages, book_id))
    print("Количество страниц изменено")

    booksDB.commit()
    booksDB.close()
    show_books()

# update_page_count(59, 1000)


#4 ЗАДАНИЕ
def delete_book(book_id):
    booksDB = sqlite3.connect("books.db")
    cursor = booksDB.cursor()

    cursor.execute("DELETE from books WHERE id =?", (book_id,))
    print("Книга удалена")

    booksDB.commit()
    booksDB.close()
    show_books()

# delete_book(55)

def  get_books_sorted_by_year():
    booksDB = sqlite3.connect("books.db")
    cursor = booksDB.cursor()

    books = cursor.execute("SELECT * FROM books ORDER BY year ASC")
    #САМОСТОЯТЕЛЬНО ИЗУЧИЛ КОМАНДУ, СОРТИРУЮЩУЮ БАЗУ ДАННЫХ ПО ОПРЕДЕЛЁННОМУ КЛЮЧУ, В НАШЕМ СЛУЧАЕ ЭТО YEAR
    print("Отсортированный по годам список книг:")
    for book in books:
        print(book)

# get_books_sorted_by_year()





