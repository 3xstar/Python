import random


el_list = []

def add_element(task):
    rand_numb = random.randint(10, 100)
    el_list.append([rand_numb, task])
    return list_elements()

def remove_element(id):
    for i in el_list:
        if i[0] == id:
            el_list.remove(i)
            break
    return list_elements()

def list_elements():
    return el_list.copy()
