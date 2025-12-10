import json
import pytest

# Фикстура для организации json-файла
@pytest.fixture
def temp_books_file(tmp_path):
    books = [
        {'id': 1, "title": "Shut up", "author": "Nigga"},
        {'id': 2, "title": "Yes im king", "author": "King"},
    ]
    file = tmp_path / 'books.json'
    file.write_text(json.dumps(books, ensure_ascii=False, indent=2))
    return str(file)