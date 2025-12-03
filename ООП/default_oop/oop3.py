class User:
    def __init__(self, name, password):
        self.name = name
        self.__password = password

user1 = User('Победа', 'qwe123456')
print(user1._User__password) # Доступ есть
print(user1.__password) # AttributeError