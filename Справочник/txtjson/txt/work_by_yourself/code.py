file = open("users.txt", "w+", encoding="utf-8")

def create_new_db():
    open("users.txt", "w+", encoding="utf-8")
    print("База данных перезаписана и очищена")

def add_user():
    with open("users.txt", "a", encoding="utf-8") as users:
        new_user = input("Введите фамилию, имя нового пользователя: ")
        content = users.write(new_user + "\n")

def show_users():
    with open("users.txt", "r+", encoding="utf-8") as users:
        print("Список пользователей:")
        list_of_users = file.read()
        print(list_of_users)

# create_new_db()
add_user()
add_user()
add_user()
show_users()
