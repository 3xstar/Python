import sqlite3
import random

shopDB = sqlite3.connect("shop.db")
cursor = shopDB.cursor()

#1 ЗАДАНИЕ
cursor.execute("CREATE TABLE IF NOT EXISTS customers"
                "(ID INTEGER,"
                "NAME TEXT,"
                "EMAIL TEXT,"
                "PHONE TEXT)")

cursor.execute("CREATE TABLE IF NOT EXISTS products"
                "(ID INTEGER,"
                "NAME TEXT,"
                "PRICE REAL,"
                "STOCK INTEGER)")

cursor.execute("CREATE TABLE IF NOT EXISTS orders"
                "(ID INTEGER,"
                "CUSTOMER_ID INTEGER,"
                "PRODUCT_ID INTEGER,"
                "QUANTITY INTEGER,"
                "ORDER_DATE TEXT)")

shopDB.close()

id = random.randint(1000,9999)

#2 ЗАДАНИЕ
def add_customer(id, name, email, phone):
    shopDB = sqlite3.connect("shop.db")
    cursor = shopDB.cursor()
    id = random.randint(1000, 9999)

    cursor.execute("INSERT INTO customers (id, name, email, phone)"
                   "VALUES (?,?,?,?)", (id, name, email, phone))

    shopDB.commit()
    shopDB.close()

def add_product(id, name, price, stock):
    shopDB = sqlite3.connect("shop.db")
    cursor = shopDB.cursor()
    id = random.randint(1000, 9999)

    cursor.execute("INSERT INTO products (id, name, price, stock)"
                   "VALUES (?,?,?,?)", (id, name, price, stock))

    shopDB.commit()
    shopDB.close()

def place_order(id, customer_id, product_id, quantity, date):
    shopDB = sqlite3.connect("shop.db")
    cursor = shopDB.cursor()
    id = random.randint(1000, 9999)

    cursor.execute("INSERT INTO orders (id, customer_id, product_id, quantity, order_date)"
                   "VALUES (?,?,?,?,?)", (id, customer_id, product_id, quantity, date))

    shopDB.commit()
    shopDB.close()

# add_customer(id, "Захар", "zaharcheg@gmail.com", "89506498724")
# add_customer(id, "Боря", "borya@mail.ru", "89455780346")
# add_customer(id, "Валера", "valerochka@gmail.com", "89674957489")
#
# add_product(id, "Snickers", "60", 8)
# add_product(id, "Red Bull", "150", 50)
# add_product(id, "Coca Cola", "80", 30)
# add_product(id, "Lays", "60", 5)
# add_product(id, "Orbit", "30", 20)

# place_order(id, 7394, 2812, 1, "24 июня")
# place_order(id, 8858, 8723, 2, "10 марта")
# place_order(id, 7933, 2695, 3, "15 октября")
# place_order(id, 7933, 6502, 5, "18 апреля")

#3 ЗАДАНИЕ
#МЫ НЕ ПРОХОДИЛИ КАК ДЕЛАТЬ ПОДОБНЫЕ ВЕЩИ, ПОЭТОМУ Я ВЗЯЛ ЭТОТ ОТРЕЗОК С НЕЙРОСЕТИ
def get_all_orders():
    shopDB = sqlite3.connect('shop.db')
    cursor = shopDB.cursor()

    client_orders = cursor.execute('''
    SELECT 
        ORDERS.ID, 
        CUSTOMERS.NAME AS CustomerName, 
        PRODUCTS.NAME AS ProductName, 
        QUANTITY, 
        ORDER_DATE 
    FROM 
        ORDERS 
    JOIN 
        CUSTOMERS ON ORDERS.CUSTOMER_ID = CUSTOMERS.ID 
    JOIN 
        PRODUCTS ON ORDERS.PRODUCT_ID = PRODUCTS.ID
    ''')
    print("Клиент и его заказы:")
    for client_order in client_orders:
        print(client_order)

    shopDB.close()
# get_all_orders()


def products_less_10():
    shopDB = sqlite3.connect("shop.db")
    cursor = shopDB.cursor()

    products = cursor.execute("SELECT name from products WHERE STOCK < 10")
    print("Продукты которых осталось меньше 10 на складе:")
    for i in products:
        print("".join(i))

    shopDB.close()
# products_less_10()


#МЫ НЕ ПРОХОДИЛИ КАК ДЕЛАТЬ ПОДОБНЫЕ ВЕЩИ, ПОЭТОМУ Я ВЗЯЛ ЭТОТ ОТРЕЗОК С НЕЙРОСЕТИ
def get_total_sum_by_customer():
    shopDB = sqlite3.connect('shop.db')
    cursor = shopDB.cursor()

    clients_sum = cursor.execute('''
    SELECT 
        CUSTOMERS.NAME, 
        SUM(PRODUCTS.PRICE * ORDERS.QUANTITY) AS TotalSum
    FROM 
        ORDERS
    JOIN 
        CUSTOMERS ON ORDERS.CUSTOMER_ID = CUSTOMERS.ID
    JOIN 
        PRODUCTS ON ORDERS.PRODUCT_ID = PRODUCTS.ID
    GROUP BY 
        CUSTOMERS.NAME
    ''')
    print("Клиент и сумма цены за покупки:")
    for client_sum in clients_sum:
        print(client_sum)

    shopDB.close()
# get_total_sum_by_customer()


def get_orders_by_customer(customer_id):
    shopDB = sqlite3.connect('shop.db')
    cursor = shopDB.cursor()

    customer_orders = cursor.execute("SELECT id, product_id, quantity, order_date"
                                     " from orders where customer_id=?", (customer_id, ))

    print("Заказы данного клиента:")
    for order in customer_orders:
        print(order)

    shopDB.close()
# get_orders_by_customer(8858)

def update_product_stock(product_id, new_stock):
    shopDB = sqlite3.connect('shop.db')
    cursor = shopDB.cursor()

    cursor.execute("UPDATE products SET stock=? where id=?", (new_stock, product_id))
    print("Количество товара обновлено.")

    shopDB.commit()
    shopDB.close()
# update_product_stock(2695, 80)

# 4 ЗАДАНИЕ
def delete_product_test():
    shopDB = sqlite3.connect('shop.db')
    cursor = shopDB.cursor()

    products = cursor.execute("SELECT * from products")
    cursor.execute("DELETE from products where id=?", (2812,))

    shopDB.commit()
    shopDB.close()
# delete_product_test()


def update_price():
    shopDB = sqlite3.connect('shop.db')
    cursor = shopDB.cursor()

    product_name = input("Введите название товара для изменения цены: ")
    new_price = int(input("Введите новую цену для этого товара: "))
    products = cursor.execute("SELECT name from products")

    for product in products:
        if "".join(product) == product_name:
            cursor.execute("UPDATE products SET price=? where name=?", (new_price, product_name))
    print("Цена изменена")

    shopDB.commit()
    shopDB.close()
# update_price()

