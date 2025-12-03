import telebot
from telebot import types
bot = telebot.TeleBot("7162634502:AAGqX63t3O67cIDFalfMQKA4ENkSUd7gSFY")

class Item:
    def __init__(self, name, description, photo, price, genre, age, article):
        self.name = name
        self.description = description
        self.photo = photo
        self.price = price
        self.genre = genre
        self.age = age
        self.article = article

    def show_info(self, id):
        bot.send_photo(id, open(self.photo, "rb"))
        buttons = types.InlineKeyboardMarkup()
        buy = types.InlineKeyboardButton("купить", callback_data=self.name)
        buttons.add(buy)
        bot.send_message(id, f"<b>{self.name}</b>\n"
                             f"<b>Описание: \n{self.description}</b>\n"
                             f"<b>Жанр: \n{self.genre}</b>\n"
                             f"<b>Возрастное ограничение: \n{self.age}</b>\n"
                             f"<b>Цена: \n{self.price}</b>\n", reply_markup=buttons)