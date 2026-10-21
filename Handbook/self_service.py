import os

ENV = os.getenv("APP_ENV", "dev")

if ENV == "dev":
    DEBUG = True
    DATABASE = "test.db"
    print("Запуск в режиме разработки")
else:
    DEBUG = False
    DATABASE = "prod.db"
    print("Запуск в боевом режиме")

def process_payment(amount):
    try:
        if amount <= 0:
            raise ValueError("Сумма должна быть положительной")
        return f"Оплачено: {amount}"
    except Exception as e:
        if DEBUG:
            print(f"Ошибка: {e}")
        else:
            with open("errors.log", "a") as f:
                f.write(f"Ошибка оплаты: {e}\n")
        return "Ошибка оплаты"

result = process_payment(100)
print(result)
result = process_payment(-50)
print(result)