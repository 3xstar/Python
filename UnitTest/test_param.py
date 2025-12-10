import pytest
from module import(add, sub, div)

def test_func():
    assert add(2, 3) == 5

def test_func2():
    assert add(6, 3) == 9

def test_func3():
    assert sub(5, 3) == 2

def test_func4():
    assert sub(14, 3) == 11

@pytest.mark.parametrize("a, b, result", [
    (2, 3, 5),
    (6, 3, 9),
    (5, 3, 8)
])

def test_add(a, b, result):
    assert add(a, b) == result

@pytest.mark.parametrize("a, b, result", [
    (3, 2, 1),
    (12, 3, 9),
    (92, 14, 78)
])

def test_sub(a, b, result):
    assert sub(a, b) == result

@pytest.mark.parametrize("a, b", [
    (3, 0),
    (12, 3),
    (0, 92)
])


def test_param_div(a, b):
    with pytest.raises(ZeroDivisionError):
        div(123, 0)