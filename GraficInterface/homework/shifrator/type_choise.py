import tkinter as tk
from tkinter import ttk
import subprocess
import sys
import os

def run_sync():
    subprocess.Popen([sys.executable, "sync_shifrator.py"])


def run_async():
    subprocess.Popen([sys.executable, "async_shifrator.py"])


def create_launcher():
    launcher = tk.Tk()
    launcher.title("Выбор типа шифрования")
    launcher.geometry("600x150")
    launcher.resizable(False, False)

    style = ttk.Style()
    style.configure('TButton', font=('Arial', 14), padding=10)

    label = ttk.Label(launcher,
                      text="🔐 Выберите тип шифрования: 🔐",
                      font=('Arial', 16))
    label.pack(pady=20)

    btn_frame = ttk.Frame(launcher)
    btn_frame.pack()

    sync_btn = ttk.Button(btn_frame,
                          text="Синхронное шифрование",
                          command=run_sync)
    sync_btn.pack(side=tk.LEFT, padx=20)

    async_btn = ttk.Button(btn_frame,
                           text="Асинхронное шифрование",
                           command=run_async)
    async_btn.pack(side=tk.RIGHT, padx=20)

    return launcher


if __name__ == "__main__":
    if not all(os.path.exists(f) for f in ["sync_shifrator.py", "async_shifrator.py"]):
        print("Ошибка: Не найдены файлы приложений!")
        sys.exit(1)

    app = create_launcher()
    app.mainloop()