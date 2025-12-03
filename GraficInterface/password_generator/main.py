import tkinter
from tkinter import ttk, messagebox
import random

class PasswordGeneratorApp: # Класс отвечает за всю функциональность приложения
    def __init__(self, window): #Инициализация приложения
        self.window = window
        self.window.geometry("500x500")
        self.window.title("Password generator")
        self.window.resizable(False, False)

        self.style = ttk.Style() #Объект для настройки стилей
        self.style.configure("TFrame", background="ghostwhite") #настройка стиля фрейма
        self.style.configure("TLabel", background="ghostwhite") #настройка стиля лейбла
        self.style.configure("header.TLabel", font=("Arial", 16, "bold"), foreground="deepskyblue3")  # настройка стиля лейбла
        self.create_widgets()

    def create_widgets(self):
        main_frame = ttk.Frame(self.window, style="TFrame")
        main_frame.pack(padx=10, pady=10, fill=tkinter.BOTH, expand=True)

        header = ttk.Label(main_frame, text="Password generator", style="header.TLabel") #настройка тега для надписи
        header.pack(pady=15)

        settings_frame = ttk.Frame(main_frame)
        settings_frame.pack(fill=tkinter.X)

        ttk.Label(settings_frame, text="Длина пароля:", font=("Arial", 17)).pack(side=tkinter.LEFT, padx=30)
        self.length = tkinter.IntVar(value=12)
        self.spin = ttk.Spinbox(settings_frame, from_=4, to=50, textvariable=self.length) #Создание блока для настройки количества символов
        self.spin.pack(side=tkinter.LEFT, padx=10)

        settings_frame2 = ttk.Frame(main_frame)
        settings_frame2.pack(fill=tkinter.X)
        ttk.Label(settings_frame2, text="Настройка сложности:", font=("Arial", 17)).pack(side=tkinter.LEFT, padx=30, pady=50)

        self.lower = tkinter.BooleanVar(value=False)
        self.upper = tkinter.BooleanVar(value=False)
        self.digit = tkinter.BooleanVar(value=False)
        self.symbol = tkinter.BooleanVar(value=False)

        ttk.Checkbutton(settings_frame2, text="Строчные буквы", variable=self.lower).pack(anchor=tkinter.CENTER, pady=10)
        ttk.Checkbutton(settings_frame2, text="Заглавные буквы", variable=self.upper).pack(anchor=tkinter.CENTER)
        ttk.Checkbutton(settings_frame2, text="Цифры", variable=self.digit).pack(anchor=tkinter.CENTER, pady=10)
        ttk.Checkbutton(settings_frame2, text="Символы", variable=self.symbol).pack(anchor=tkinter.CENTER)

if __name__ == "__main__":
    window = tkinter.Tk()
    add = PasswordGeneratorApp(window)
    window.mainloop()

