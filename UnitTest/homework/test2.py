from func2 import *


def testAdd():
    el_list.clear()
    add_element("простая задача")
    assert len(el_list) == 1


def testRemove():
    el_list.clear()
    add_element("удалить эту задачу")
    id_to_remove = el_list[0][0]

    remove_element(id_to_remove)
    assert len(el_list) == 0


def testEmptyInput():
    el_list.clear()
    add_element("")
    assert el_list[0][1] == ""


def testCopy():
    el_list.clear()
    add_element("повтор")
    add_element("повтор")
    assert len(el_list) == 2
    assert el_list[0][1] == "повтор"
    assert el_list[1][1] == "повтор"