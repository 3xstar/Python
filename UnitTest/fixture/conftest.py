import pytest
# Фикстура - заготовка для теста
@pytest.fixture
def music_data():
    music =[
        {"id": 1, "name": "track_1", "duration": 192},
        {"id": 2, "name": "track_2", "duration": 175},
        {"id": 3, "name": "track_3", "duration": 149}
    ]
    return music

def test_fixture(music_data):
    assert music_data[0]["name"] == "track_1"
    assert len(music_data) > 1