import telebot
from user import *
from item import *
import sqlite3
import os
from dotenv import load_dotenv

load_dotenv()
bot = telebot.TeleBot(os.getenv("TOKEN"))
requests_bot = telebot.TeleBot(os.getenv("REQUEST_TOKEN"))
admin_id = os.getenv("ADM_ID")

usersDB = sqlite3.connect("users.db")
cursor = usersDB.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS users"
               "(id INTEGER, "
               "name TEXT, "
               "username TEXT, "
               "age INTEGER, "
               "promocode TEXT)")

cursor.execute("CREATE TABLE IF NOT EXISTS orders"
               "(id INTEGER, "
               "article TEXT)")

usersDB.close()

itemsDB = sqlite3.connect("items.db")
cursor = itemsDB.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS items"
               "(name TEXT, "
               "description TEXT, "
               "photo TEXT, "
               "price INTEGER, "
               "genre TEXT, "
               "age INTEGER, "
               "article INTEGER)")

itemsDB.close()

def add_items_db(item:Item):
    itemsDB = sqlite3.connect("items.db")
    cursor = itemsDB.cursor()

    cursor.execute("INSERT INTO items (name, description, photo, price, genre, age, article)"
                   "VALUES (?, ?, ?, ?, ?, ?, ?)",
                   (item.name, item.description, item.photo, item.price, item.genre, item.age, item.article))
    itemsDB.commit()
    itemsDB.close()

def get_items_db(items):
    itemsDB = sqlite3.connect("items.db")
    cursor = itemsDB.cursor()

    cursor.execute("SELECT * FROM items")
    items_db = cursor.fetchall()

    for item in items_db:
        item_class = Item(item[0], item[1], item[2], item[3], item[4], item[5], item[6])
        items.append(item_class)

    itemsDB.close()
    return items

# gta = Item("GTA", "игра для народа",
#            "photos/gta.jpg", 1000,
#            "action", "6+", 1001)
#
# witcher = Item("Witcher 3", "игра для борцов со злом",
#            "photos/witcher.jpg", 800,
#            "action", "6+", 1002)
#
# wukong = Item("Wukong", "игра для Влада",
#            "photos/wukong.jpg", 2500,
#            "action", "1+", 1003)
#
# add_items_db(gta)
# add_items_db(witcher)
# add_items_db(wukong)

users = []
items = []

items = get_items_db(items)

def get_info_db(users):
    usersDB = sqlite3.connect("users.db")
    cursor = usersDB.cursor()

    cursor.execute("SELECT * FROM users")

    users_DB = cursor.fetchall()

    for user in users_DB:
        userClass = User(user[0], user[1], user[1])
        userClass.age = user[3]
        userClass.promocodes = user[4]

        users.append(userClass)

    usersDB.close()
    return users

def add_into_db(user:User):
    usersDB = sqlite3.connect("users.db")
    cursor = usersDB.cursor()

    cursor.execute("INSERT INTO users (id, name, username, age, promocode)"
                   "VALUES (?, ?, ?, ?, ?)", (user.id, user.name, user.username, user.age, user.promocodes))

    usersDB.commit()
    usersDB.close()

def get_orders_db(user):
    orders = []
    usersDB = sqlite3.connect("users.db")
    cursor = usersDB.cursor()
    cursor.execute("SELECT article FROM orders WHERE id = ?", (user.id,))
    orders = cursor.fetchall()[0].split

    usersDB.close()
    return orders


def set_orders_db(orders, id):
    usersDB = sqlite3.connect("users.db")
    cursor = usersDB.cursor()

    orders_str = " ".join(orders)

    cursor.execute("SELECT id FROM orders")
    all_id = cursor.fetchall()

    if id in all_id:
        cursor.execute("UPDATE orders SET article = ? WHERE id = ?", (orders_str, id))
    else:
        cursor.execute("INSERT INTO ORDERS (id, article) VALUES (?, ?)", (id, orders_str))

    usersDB.close()

users = get_info_db(users)

@bot.message_handler(content_types=["sticker"])
def main(message):
    bot.send_sticker(message.chat.id, sticker="CAACAgIAAxkBAAM_Z9EN4VyMT70acUfxYBknRpTNZ2QAAtcRAALyVshLFA73w0_WuYs2BA")

@bot.message_handler(commands=["start", "help"])
def main(message):
    if not check_user(message.from_user.id):
        new_user = User(message.from_user.id,
                        message.from_user.first_name,
                        message.from_user.username)
        users.append(new_user)
        add_into_db(new_user)

    # bot.send_message(message.chat.id, message.from_user.id) Узнать айди
    bot.send_message(message.chat.id, "Добро пожаловать в GameShopBot! Получайте лучшие игры по лучшим ценам, только у нас)")
    menu_button = types.InlineKeyboardMarkup()
    shop = types.InlineKeyboardButton("посмотреть товары", callback_data="shop")
    admin = types.InlineKeyboardButton("обратиться к админу", callback_data="admin")
    edit_profile = types.InlineKeyboardButton("редактировать профиль", callback_data="edit_profile")
    my_orders = types.InlineKeyboardButton("мои заказы", callback_data="my_orders")
    user_profile = types.InlineKeyboardButton("информация о пользователе", callback_data="user_profile")

    for button in shop, admin, edit_profile, my_orders, user_profile:
        menu_button.row(button)

    bot.send_message(message.chat.id, "Выберите нужный пункт меню", reply_markup=menu_button)

@bot.callback_query_handler(func=lambda callback: True)
def main(callback):
    id = callback.message.chat.id

    for item in items:
        if item.name == callback.data:
            item.show_info(id)

    match callback.data:
        case "shop":
            show_items(items, id)

        case "admin":
            bot.send_message(id, "обращение к админу")
            call_admin(callback.message)

        case "edit_profile":
            bot.send_message(id, "редактирование профиля")

        case "my_orders":
            bot.send_message(id, "список ваших заказов")

        case "user_profile":
            for user in users:
                if user.id == callback.from_user.id:
                    user.show_info(user.id)
                    break

        # case _:
        #     bot.send_message(id, "данная функция еще в разработке, извините :<")

def call_admin(message):
    message = bot.send_message(message.chat.id,"Опишите вашу проблему: ")
    bot.register_next_step_handler(message, send_admin)

def send_admin(message):
    bot.send_message(message.chat.id, "Данные отправлены администратору, в скором времени он с вами свяжется :з")
    requests_bot.send_message(admin_id, f"Запрос от @{message.from_user.username}\n"
                               f"Обращение: {message.text}")

def check_user(id):
    is_User = False
    for user in users:
        if user.id == id:
            is_User = True
            break
    return is_User

def show_items(items, id):
    games = types.InlineKeyboardMarkup()
    for item in items:
        game = types.InlineKeyboardButton(item.name, callback_data=item.name)
        games.row(game)
    bot.send_message(id, "список игр: ", reply_markup=games)

bot.polling()
