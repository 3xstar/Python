log_list = []
list_user = []

class User:
    def __init__(self, name, list_log, user_list):
        self.name = name
        list_log.append(f"Создан пользователь под именем: {self.name}")
        user_list.append(self.name)

    def greeting(self):
        return f"Привет пользователь {self.name}"


class Admin(User):
    def __init__(self, name, permission=None):
        super().__init__(name, log_list, list_user)
        if permission is None:
            permission = ["удаление", "редактирование"]
        self.name = name
        self.permission = permission

    def greeting(self):
        text = "".join([f"\n{item}" for item in self.permission])
        return f"{super().greeting()} - теперь ты админ и имеешь следующие функции: {text}"

    def print_user(self, user_list):
        print("Список пользователей:")
        for i in user_list:
            print(f"\n{i}")

    def delete_user(self, user_list, list_log):
        count = 1
        print("Список пользователей с нумерацией:")
        for i in user_list:
            print(f"\n{count, i}")
            count += 1
        user_for_del = int(input("Введите номер пользователя для удаления: "))
        if 1 <= user_for_del <= count:
            user_list.remove(user_list[user_for_del - 1])
            list_log.append(f"Пользователь под именем: {self.name} удален")
        return user_list

    def edit_user(self, user_list, list_log):
        count = 1
        print("Список пользователей с нумерацией:")
        for i in user_list:
            print(f"\n{count, i}")
            count += 1
        user_for_find = int(input("Введите номер пользователя для редактирования: "))
        if 1 <= user_for_find <= count:
            new_user = input("Введите новое имя пользователя: ")
            user_list[user_for_find - 1], new_user = new_user, user_list[user_for_find - 1]
            list_log.append(f"Имя пользователя {user_list[user_for_find - 1]} изменено на {new_user}")
        return user_list


class Moder(User):
    def __init__(self, name, permission=None):
        super().__init__(name, log_list, list_user)
        if permission is None:
            permission = ["удаление", "просмотр"]
        self.name = name
        self.permission = permission

    def greeting(self):
        text = "".join([f"\n{item}" for item in self.permission])
        return f"{super().greeting()} - теперь ты модератор и имеешь следующие функции: {text}"

    def print_user(self, user_list):
        print("Список пользователей:")
        for i in user_list:
            print(f"\n{i}")

    def delete_user(self, user_list, list_log):
        count = 1
        print("Список пользователей с нумерацией:")
        for i in user_list:
            print(f"\n{count, i}")
            count += 1
        user_for_del = int(input("Введите номер пользователя для удаления: "))
        if 1 <= user_for_del <= count:
            user_list.remove(user_list[user_for_del - 1])
            list_log.append(f"Пользователь под именем: {self.name} удален")
        return user_list


class Visitor(User):
    def __init__(self, name, permission=None):
        super().__init__(name, log_list, list_user)
        if permission is None:
            permission = ["чтение", "просмотр"]
        self.name = name
        self.permission = permission

    def print_user(self, user_list):
        print("Список пользователей:")
        for i in user_list:
            print(f"\n{i}")

    def greeting(self):
        text = "".join([f"\n{item}" for item in self.permission])
        return f"{super().greeting()} - теперь ты посетитель и имеешь следующие функции: {text}"


user = User("Александр", list_log=log_list, user_list=list_user)
admin = Admin("Степа")
moder = Moder("Валера")
visitor = Visitor("Боря")

print(log_list)
print(list_user)