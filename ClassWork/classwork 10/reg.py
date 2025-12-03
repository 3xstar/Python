users = set()


def show_all(users):
    if users:
        for user in users:
            print(user)
    else:
        print("нету пользователей")


def add_user(users):
    name = input("введите имя пользователя")
    users.add(name)
    print("пользователь добавлен")
    return users



def delete_user(users):
    name = input("введите имя пользователя")
    users.remove(name)
    print("пользователь удален")
    return users

while True:
    print("1. Вывести всех пользователей \n"
          "2. Добавить пользователей \n"
          "3. Удалить пользователя")
    action = int(input("Введите номер команды: "))

    match action:
        case 1:
            show_all(users)
        case 2:
            users = add_user(users)
        case 3:
            users = delete_user(users)
        case _:
            print("такой команды нет")
