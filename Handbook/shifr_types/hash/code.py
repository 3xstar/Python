import os
from hashlib import pbkdf2_hmac

# Генерация соли
salt = os.urandom(16)  # Уникальная соль для каждого пароля
password = "мой_пароль".encode()

# Хеширование с 100,000 итерациями
hashed = pbkdf2_hmac(
    'sha256',
    password,
    salt,
    100000,
    dklen=32  # Длина ключа 32 байта
)

print("Соль:", salt.hex())
print("Хеш:", hashed.hex())

# Проверка пароля (пример)
def verify_password(input_pass, stored_salt, stored_hash):
    new_hash = pbkdf2_hmac('sha256', input_pass.encode(), stored_salt, 100000)
    return new_hash == stored_hash

# Тест
print("Пароль верен?", verify_password("data", salt, hashed))