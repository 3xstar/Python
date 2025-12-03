import tkinter
from tkinter import *
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding as sym_padding
from tkinter import filedialog, messagebox
import os

window = Tk()
window.title("Shifrator")
window.geometry("800x300")
window.resizable(False, False)

private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
public_key = private_key.public_key()


def encrypt(data):
    aes_key = os.urandom(32)
    iv = os.urandom(16)

    cipher = Cipher(algorithms.AES(aes_key), modes.CBC(iv))
    encryptor = cipher.encryptor()
    padder = sym_padding.PKCS7(128).padder()

    padded_data = padder.update(data) + padder.finalize()
    encrypted_data = encryptor.update(padded_data) + encryptor.finalize()

    encrypted_key = public_key.encrypt(
        aes_key,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    return iv + encrypted_key + encrypted_data


def decrypt(encrypted_data):
    iv = encrypted_data[:16]
    encrypted_key = encrypted_data[16:272]
    encrypted_data = encrypted_data[272:]

    aes_key = private_key.decrypt(
        encrypted_key,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    cipher = Cipher(algorithms.AES(aes_key), modes.CBC(iv))
    decryptor = cipher.decryptor()
    unpadder = sym_padding.PKCS7(128).unpadder()

    decrypted_data = decryptor.update(encrypted_data) + decryptor.finalize()
    unpadded_data = unpadder.update(decrypted_data) + unpadder.finalize()

    return unpadded_data


Label(text="🔓Shifrator🔒", font=("Arial", 20), fg="green").pack(pady=10)
Label(text="Путь файла для операции:", font=("Arial", 20)).pack()
entry = Entry(font=("Arial", 12), width=60, background="gray75", state="readonly")
entry.pack(pady=10)


def ask_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        entry.config(state="normal")
        entry.delete(0, END)
        entry.insert(0, file_path)
        entry.config(state="readonly")


def encrypt_script():
    try:
        with open(entry.get(), "rb") as file:
            file_data = file.read()

        encrypted_data = encrypt(file_data)

        with open(entry.get() + ".rsa", "wb") as file:
            file.write(encrypted_data)

        os.remove(entry.get())
        messagebox.showinfo("Успех", "Файл зашифрован!")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Ошибка при шифровании: {str(e)}")


def decrypt_script():
    try:
        if not entry.get().endswith('.rsa'):
            messagebox.showerror("Ошибка", "Файл должен иметь расширение .rsa")
            return

        with open(entry.get(), "rb") as file:
            encrypted_data = file.read()

        decrypted_data = decrypt(encrypted_data)

        output_path = entry.get()[:-4]
        with open(output_path, "wb") as file:
            file.write(decrypted_data)

        os.remove(entry.get())
        messagebox.showinfo("Успех", "Файл расшифрован!")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Ошибка при дешифровании: {str(e)}")


ask_file_button = Button(text="Выбрать файл", font=("Arial", 17), command=ask_file)
ask_file_button.pack(pady=20)

Button(text="Зашифровать файл", font=("Arial", 17), background="red", command=encrypt_script).pack(side=tkinter.LEFT,
                                                                                                   padx=30)
Button(text="Расшифровать файл", font=("Arial", 17), background="green", command=decrypt_script).pack(
    side=tkinter.RIGHT, padx=30)

window.mainloop()