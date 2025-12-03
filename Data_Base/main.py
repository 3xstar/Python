import sqlite3

users = sqlite3.connect("users.db")

#создание курсора
cursor = users.cursor()

#создание таблицы
#cursor.execute("CREATE TABLE users (name TEXT, "
#               "id INTEGER, "
#               "age INTEGER )")

#записать данные в таблицу
#cursor.execute("INSERT INTO users VALUES('Solovyov Zahar', 457896, 17)")

#сохранить изменения в базу данных
#users.commit()

#вытащить всё
cursor.execute("SELECT * FROM users")
print(cursor.fetchall())

#вытащить имена
cursor.execute("SELECT name FROM users")
print(cursor.fetchall())

#вытащить порядковые номера элементов
cursor.execute("SELECT rowid, name, id FROM users")
print(cursor.fetchall())

#вытащить n количество строк
cursor.execute("SELECT * FROM users")
print(cursor.fetchone())
print(cursor.fetchone())

#удалить элемент
#cursor.execute("DELETE FROM users WHERE id = '457896'")

users.close()