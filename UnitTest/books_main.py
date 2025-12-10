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