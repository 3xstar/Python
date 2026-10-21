# Сделать простой класс для управления банковским аккаунтом и заприватить в нем баланс, класс должен содержать следующие функции:
# - Перевод денег с одного аккаунта на другой;
# - Пополнение баланса;
# - Снятие баланса.
# На каждое действие должны быть проверки
# Добавить статический метод для отображения информации о классе или о финансовой грамотности

def show_info():
    print("Класс Bank предназначен для симулирования денежных операций, он умеет продумывать разные ситуации чтобы"
          "выявлять ошибки и имеет следующий функионал: \n"
          "Перевод денег с одного аккаунта на другой\n"
          "Пополнение баланса\n"
          "Снятие баланса")


class Bank:
    def __init__(self, balance=None):
        self.balance = balance if balance is not None else 0

    def add_balance(self):
        money = int(input("Введите количество денег для пополнения баланса: "))

        if money > 0:
            self.balance += money
            print("Деньги были начислены на баланс")
        elif money <= 0:
            print("Операция не была выполнена\n"
                  "Причина: количество денег для пополнения меньше либо равно нулю")
        else:
            print("Операция не была выполнена\n"
                  "Причина: непредвиденная ошибка")

        print("Текущий баланс:", self.balance)
        return self.balance

    def balance_away(self):
        minus_money = int(input("Введите количество денег для снятия с баланса: "))

        if 0 < minus_money <= self.balance:
            self.balance -= minus_money
            print("Деньги были сняты с баланса")
        else:
            if minus_money == 0:
                print("Операция не была выполнена\n"
                      "Причина: количество денег для снятия меньше либо равно нулю")
            elif minus_money > self.balance:
                print("Операция не была выполнена\n"
                      "Причина: вы не можете снять с баланса больше, чем у вас есть на балансе")
            else:
                print("Операция не была выполнена\n"
                      "Причина: непредвиденная ошибка")

        print("Текущий баланс:", self.balance)
        return self.balance

    def send_money(self):
        account_name = input("Введите название аккаунта для перевода баланса: ")
        account_balance = 0
        money_for_account = int(input(f"Введите количество денег для перевода на {account_name}:"))
        if 0 < money_for_account <= self.balance:
            self.balance -= money_for_account
            account_balance += money_for_account
            print(f"Сумма {money_for_account} была переведена на {account_name}")
        else:
            if money_for_account == 0:
                print("Операция не была выполнена\n"
                      "Причина: количество денег для снятия меньше либо равно нулю")
            elif money_for_account > self.balance:
                print("Операция не была выполнена\n"
                      "Причина: вы не можете снять с баланса больше, чем у вас есть на балансе")
            else:
                print("Операция не была выполнена\n"
                      "Причина: непредвиденная ошибка")
        print("Текущий баланс:", self.balance)

