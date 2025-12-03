import random
class Items:
    def __init__(self, name, price, article):
        self.name = name
        self.price = price
        self.article = article

        self.id = None
        self.status = None
        self.order_id = None

    def show_info(self):
        print(f"название: {self.name} \n,"
              f"цена: {self.price} \n,"
              f"артикул: {self.article}")

        if self.id:
            print(f"статус заказа: {self.status} \n"
                  f"номер заказа {self.order_id}")

    def buy_item(self, id):
        self.id = id
        self.status = "заказан"
        self.order_id = random.randint(100,999)