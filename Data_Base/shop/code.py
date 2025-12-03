import sqlite3
from items import *
from users import *

users_db = sqlite3.connect("shop_users.db")
cursor = users_db.cursor()

statuses = ["заказан", "в пути", "на пункте выдачи", "завершен"]

cursor.execute("CREATE TABLE IF NOT EXISTS Users "
               "(id INTEGER, "
               "name TEXT, "
               "username TEXT, "
               "age INTEGER, "
               "email TEXT)")

cursor.execute("CREATE TABLE IF NOT EXISTS Orders"
               "(id INTEGER, "
               "name TEXT, "
               "price INTEGER, "
               "status TEXT, "
               "article INTEGER, "
               "order_id INTEGER)")

users_db.commit()
users_db.close()

user1 = Users(1321451, "BolekaAmbalabu", "@lyagushka", 25, "kwa@gmail.com")
user2 = Users(5893496, "TralaleloTralala", "@akula", 30, "kus@gmail.com")

item1 = Items("Zahar", 10, 43425)
item2 = Items("Dima", 1, 89023)

def add_users_DB(user: Users):
    users_db = sqlite3.connect("shop_users.db")
    cursor = users_db.cursor()

    cursor.execute("INSERT INTO Users (id, name, username, age, email)"
                   "VALUES (?, ?, ?, ?, ?)", user.get_info())

    users_db.commit()
    users_db.close()

def buy_item(user: Users, item: Items):
    item.buy_item(user.id)

    users_db = sqlite3.connect("shop_users.db")
    cursor = users_db.cursor()

    cursor.execute("INSERT INTO Orders (id, name, price, article, status, order_id)"
                   "VALUES (?, ?, ?, ?, ?, ?)", (user.id, item.name, item.price,
                   item.article, item.status, item.order_id))

    users_db.commit()
    users_db.close()

def show_orders(user: Users):
    with sqlite3.connect("shop_users.db") as users_db:
        cursor = users_db.cursor()
        cursor.execute("SELECT * FROM Orders Where id=?", (user.id, ))

        orders = cursor.fetchall()
        if orders:
            for order in orders:
                if order[4] != statuses[len(statuses) - 1]:
                    print(f"Название: {order[1]} \n"
                          f"Цена: {order[2]} \n"
                          f"Статус: {order[3]} \n"
                          f"Артикул: {order[4]} \n"
                          f"ID заказа: {order[5]}")

def up_status(user: Users, order_id):
    with (sqlite3.connect("shop_users.db") as users_db):
        cursor = users_db.cursor()
        cursor.execute("SELECT status FROM Orders WHERE order_id=?", (order_id, ))

        order_status = cursor.fetchone()[0]

        if order_status != "завершен":
            next_status = statuses[statuses.index(order_status) + 1]
        else:
            next_status = order_status

        cursor.execute("UPDATE Orders SET status=? WHERE order_id=?", (next_status, order_id))

        users_db.commit()

# add_users_DB(user1)
# add_users_DB(user2)
# buy_item(user1, item1)
# buy_item(user2, item2)
up_status(user1, 161)
show_orders(user1)