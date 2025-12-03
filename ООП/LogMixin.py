list_log = []

class LogMixin:
    def log_message(self, message, list):
        print(f"[LOG: {message} ]")
        list.append(message)

class Database:
    def save(self):
        print("Данные сохранены")

class DatabaseOperation(Database, LogMixin):
    def get_data(self):
        super().save()
        self.log_message("Запрос на получение данных", list_log)

    def add_data(self):
        super().save()
        self.log_message("Запрос на отправку данных", list_log)

do = DatabaseOperation()
do.get_data()
do.add_data()
print(list_log)