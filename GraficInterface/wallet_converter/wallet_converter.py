from tkinter import *
import requests


def get_currency_rates(valute):
    url = "https://www.cbr-xml-daily.ru/daily_json.js"
    response = requests.get(url)
    data = response.json()
    return data["Valute"][valute]["Value"]


window = Tk()
window.title("Конвертер валют")
window.geometry("600x300")
window.resizable(False, False)

for c in range(4):
    window.columnconfigure(index=c, weight=1)
for r in range(4):
    window.rowconfigure(index=r, weight=1)


def convert_USD():
    if entry.get().isdigit():
        result["text"] = f"{round(float(entry.get()) / get_currency_rates('USD'), 3)} $"
    else:
        result.config(text="Вы ввели некорректные значения")


def convert_EURO():
    if entry.get().isdigit():
        result["text"] = f"{round(float(entry.get()) / get_currency_rates('EUR'), 3)} €"
    else:
        result.config(text="Вы ввели некорректные значения")


def repeated():
    if len(entry.get()) > 20:
        entry.delete(len(entry.get()) - 1)
        window.update()

    window.after(50, repeated)


label = Label(window, text="Wallet Converter", font=("Arial", 20), background="green", fg="white")
label.grid(row=0, column=1, columnspan=2, pady=10)

entry = Entry(window, font=("Arial", 15))
entry.grid(row=1, column=0, columnspan=2, padx=0)

convert_USD = Button(window, text="Convert to USD", command=convert_USD, width=15)
convert_USD.grid(row=1, column=2)

convert_EURO = Button(window, text="Convert to EURO", command=convert_EURO, width=15)
convert_EURO.grid(row=2, column=2)

result = Label(window, text="", font=("Arial", 20), background="gray75", width=30)
result.grid(row=4, column=1, columnspan=2)

window.after(0, repeated)
window.mainloop()
