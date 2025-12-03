class User:
    def __init__(self, name, password):
        self.name = name
        self.password = password

    def getPassword(self):
        return self.password
    
    def setPassword(self, value):
        if len(value) > 3:
            self.password = value
        else:
            print("Говно!")

# Выше - устаревший вариант, ниже - современный

class User:
    def __init__(self, name, password):
        self.name = name
        self.password = password

    @property
    def getPassword(self):
        return self.password # Возвращаем результат
    
    @getPassword.setter
    def setPassword(self, value):
        if len(self.password) > 3:
            self.password = value # Фиксируем получение данных
        else:
            print("Говнище!")