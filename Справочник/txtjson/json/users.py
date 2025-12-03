import json


class User:
    def __init__(self, name, surname, jobs):
        self.name = name
        self.surname = surname
        self.jobs = jobs


def create_user():
    name = input("Введите имя пользователя: ")
    surname = input("Введите фамилию пользователя: ")
    jobs = input("Введите места работы пользователя: ")
    new_user = User(name=name, surname=surname, jobs=jobs)
    with open(f"{name}.json", "w+", encoding="utf-8") as file:
        json.dump(new_user.__dict__, file, ensure_ascii=False, indent=2)


# create_user()

def change_user():
    user = input("Введите название json файла для изменения: ")
    with open(f"{user}.json", "w+", encoding="utf-8") as file:
        name = input("Введите новое имя пользователя: ")
        surname = input("Введите новую фамилию пользователя: ")
        jobs = input("Введите новые места работы пользователя: ")
        new_user = User(name=name, surname=surname, jobs=jobs)
        with open(f"{user}.json", "w+", encoding="utf-8") as file:
            json.dump(new_user.__dict__, file, ensure_ascii=False, indent=2)

# change_user()
