import threading
import time

def time_sleep1():
    time.sleep(10)
    print("\nПрошло 10 секунд")

def time_sleep2():
    time.sleep(20)
    print("\nПрошло 20 секунд")

timer = input("Время для таймера: \n"
             "1. 10 секунд\n"
             "2. 20 секунд\n"
              "Выберите номер: ")

if timer == "1":
    t1 = threading.Thread(target=time_sleep1())
    t1.start()
elif timer == "2":
    t2 = threading.Thread(target=time_sleep2())
    t2.start()
else:
    print("Неверная команда")