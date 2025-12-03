class Users:
    def __init__(self, id, name, username, age, email):
        self.id = id
        self.name = name
        self.username = username
        self.age = age
        self.email = email

    def show_info(self):
        print(f"имя: {self.name} \n,"
              f"возраст: {self.age} \n,"
              f"почта: {self.email}")

    def get_info(self):
        return self.id, self.name, self.username, self.age, self.email