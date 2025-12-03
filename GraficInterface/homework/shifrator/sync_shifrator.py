import tkinter
from tkinter import *
from cryptography.fernet import Fernet
import base64
from hashlib import sha256
import os
from tkinter import filedialog, messagebox

window = Tk()
window.title("Shifrator")
window.geometry("800x400")
window.resizable(False, False)

def generate_key(key_path):
    key = Fernet.generate_key()
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
    try:
        key = sha256(key.encode()).digest()
        shifrator = Fernet(base64.urlsafe_b64encode(key))

        with open(file_path, "rb",) as file:
            file_data = file.read()

        encrypt_data = shifrator.encrypt(file_data)

        with open(file_path + ".enc", "wb",) as file:
            file.write(encrypt_data)

        os.remove(file_path)
        messagebox.showinfo(title="Успех", message="Файл зашифрован")

    except Exception as e:
        messagebox.showerror("Ошибка", f"Ошибка при шифровании: {str(e)}")

def decrypt_file(file_path, key):
    try:
        if not entry1.get().endswith('.enc'):
            messagebox.showerror("Ошибка", "Файл должен иметь расширение .enc")
            return

        key = sha256(key.encode()).digest()
        shifrator = Fernet(base64.urlsafe_b64encode(key))

        with open(file_path, "rb",) as file:
            file_data = file.read()
        decrypt_data = shifrator.decrypt(file_data)
        output_path = file_path.replace(".enc", "")

        with open(output_path, "wb") as file:
            file.write(decrypt_data)
        os.remove(file_path)
        messagebox.showinfo(title="Успех", message="Файл расшифрован")

    except Exception as e:
        messagebox.showerror("Ошибка", f"Ошибка при дешифровании: {str(e)}")

Label(text="🔓Shifrator🔒", font=("Arial", 20), fg="green").pack(pady=10)

Label(text="Путь файла для операции:", font=("Arial", 20)).pack()
entry1 = Entry(font=("Arial", 12), width=60, background="gray75", state="readonly")
entry1.pack(pady=10)

def ask_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        entry1.config(state="normal")
        entry1.delete(0, END)
        entry1.insert(0, file_path)
        entry1.config(state="readonly")

def insert_key(key):
    entry2.delete(0, END)
    entry2.insert(0, key)

def encrypt_script():
    key = load_key()
    insert_key(key=key)
    encrypt_file(file_path=entry1.get(), key=key)

def decrypt_script():
    decrypt_file(file_path=entry1.get(), key=entry2.get())
    entry2.delete(0, END)

ask_file_button = Button(text="Выбрать файл", font=("Arial", 17), command=ask_file)
ask_file_button.pack(pady=20)

Label(text="Ключ (СОХРАНИТЕ!!!)", font=("Arial", 20), fg="gold").pack()
entry2 = Entry(font=("Arial", 12), width=60, background="gray75")
entry2.pack()

Button(text="Зашифровать файл", font=("Arial", 17), background="red", command=encrypt_script).pack(side=tkinter.LEFT, padx=70)
Button(text="Расшифровать файл", font=("Arial", 17), background="green", command=decrypt_script).pack(side=tkinter.RIGHT, padx=70)

window.mainloop()