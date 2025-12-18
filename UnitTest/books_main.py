from books import(
load_books,
save_books,
add_book,
delete_book,
update_book,
find_book
)

def test_load_books(temp_books_file):
    books = load_books(temp_books_file)
    assert  len(books) == 2
    assert books[0]["title"] == 'Shut up'

def test_add_book(temp_books_file):
    new = {"id": 3, "title": "Sigma Ohio", "author": "Don Pollo"}
    add_book(temp_books_file, new)
    books = load_books(temp_books_file)
    assert len(books) == 3
    assert books[-1]["title"] == "Sigma Ohio"


def test_delete_book(temp_books_file):
    book_id = 2
    delete_book(temp_books_file, book_id)
    books = load_books(temp_books_file)
    assert len(books) == 1

def test_update_book(temp_books_file):
    book_id = 1
    update_data = {"title": "Diddy blud"}
    result = update_book(temp_books_file, book_id, update_data)
    assert result == True

def test_find_book(temp_books_file):
    book_title = 'Shut up'
    books = load_books(temp_books_file)
    result = find_book(temp_books_file, book_title)
    assert result["title"] == book_title

