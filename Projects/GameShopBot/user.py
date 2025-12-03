import telebot
bot = telebot.TeleBot("7162634502:AAGqX63t3O67cIDFalfMQKA4ENkSUd7gSFY")

class User:
    def __init__(self, id, name, username):
        self.id = id
        self.name = name
        self.username = username
        self.age = None
        self.orders = []
        self.basket = []
        self.promocodes = "NewUser"

    def show_info(self, id):
        bot.send_message(id, f"Имя: {self.name} \n"
                             f"Тег: {self.username} \n"
                             f"Возраст: {self.age}")

    def show_orders(self):
        if len(self.orders):
            for order in self.orders:
                bot.send_message(self.id, order)
        else:
            bot.send_message(self.id, "Вы пока-что ничего не заказали :(")

    def show_basket(self):
        if len(self.basket):
            for item in self.basket:
                bot.send_message(self.id, item)
        else:
            bot.send_message(self.id, "Вы пока что ничего не добавили :(")