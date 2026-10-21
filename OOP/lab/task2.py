from abc import  *

class Account(ABC):
    def __init__(self, balance):
        self.balance = balance

    def deposit(self):
        deposit = int(input("Введите сумму депозита: "))
        self.balance += deposit
        print(f"На баланс зачислено: {deposit}")

    def withdraw(self):
        withdraw = int(input("Введите сумму вывода: "))
        self.balance -= withdraw
        print(f"С баланса выведено: {withdraw}")

    def get_balance(self):
        return self.balance

class SavingsAccount(Account):
    def __init__(self, balance):
        super().__init__(balance)
        self.balance = balance

    def deposit(self):
        deposit = int(input("Введите сумму депозита: "))
        self.balance += deposit
        print(f"На баланс зачислено: {deposit}")

    def withdraw(self):
        withdraw = int(input("Введите сумму вывода: "))
        if self.balance < withdraw:
            print("У вас нет возможности уйти в минус")
            return 0
        self.balance -= withdraw
        print(f"С баланса выведено: {withdraw}")

    def get_balance(self):
        return self.balance


class CreditAccount(Account):
    def __init__(self, balance, percent_rate):
        super().__init__(balance)
        self.percent_rate = percent_rate
        self.balance = balance

    def deposit(self):
        deposit = int(input("Введите сумму депозита: "))
        self.balance += deposit
        if self.balance < 0:
            self.percent_rate += 1
            self.balance -= ((self.balance / 100) * self.percent_rate)
            print(f"На баланс зачислено: {deposit}, процентная ставка увеличена до: {self.percent_rate}")

        else:
            print(f"На баланс зачислено: {deposit}, процентная ставка: {self.percent_rate}")

    def withdraw(self):
        withdraw = int(input("Введите сумму вывода: "))
        self.balance -= withdraw
        if self.balance < 0:
            self.percent_rate += 1
            self.balance -= ((self.balance / 100) * self.percent_rate)
            print(f"С баланса выведено: {withdraw}, процентная ставка увеличена до: {self.percent_rate}")

        else:
            print(f"С баланса выведено: {withdraw}, процентная ставка: {self.percent_rate}")

    def get_balance(self):
        return self.balance



loh = CreditAccount(1000, 0)
loh.withdraw()
print(loh.get_balance())
loh.withdraw()
print(loh.get_balance())
