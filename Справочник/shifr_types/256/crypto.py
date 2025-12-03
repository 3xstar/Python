from cryptography.fernet import Fernet
import base64
from hashlib import sha256
import os

def generate_key(key_path):
    key = Fernet.generate_key() #генерация ключа
    with open(key_path, "wb") as file:
        file.write(key)
    return str(key)


def load_key(key_path = "secret.key"):
    if os.path.exists(key_path):
        with open(key_path, "rb") as file:
            return str(file.read())
    else:
        return generate_key(key_path)


def encrypt_file(file_path, key):
    key = sha256(key.encode()).digest()
    print("Закодированный ключ: ", key)
    shifrator = Fernet(base64.urlsafe_b64encode(key)) #добавление шифратора

    with open(file_path, "rb",) as file:
        file_data = file.read()

    encrypt_data = shifrator.encrypt(file_data)

    with open(file_path + ".enc", "wb",) as file:
        file.write(encrypt_data)

    os.remove(file_path)
    print("Файл зашифрован")


def decrypt_file(file_path, key):
    key = sha256(key.encode()).digest()
    shifrator = Fernet(base64.urlsafe_b64encode(key))  # добавление шифратора

    with open(file_path, "rb",) as file:
        file_data = file.read()
    try:
        decrypt_data = shifrator.decrypt(file_data)
        output_path = file_path.replace(".enc", "")

        with open(output_path, "wb") as file:
            file.write(decrypt_data)
        os.remove(file_path)
        print("Файл расшифрован")
    except:
        print("Ошибка")


load_key()
# encrypt_file("C:\\Users\\tmrni\\Downloads\\images.jpg", load_key("C:\\Users\\tmrni\\Downloads\\secret.key"))
# decrypt_file("C:\\Users\\tmrni\\Downloads\\images.jpg.enc", load_key("C:\\Users\\tmrni\\Downloads\\secret.key"))