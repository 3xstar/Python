from tkinter import *

window = Tk()
window.title("Calculator")
window.geometry("300x600")
window.resizable(False, False)

def plus():
    if entry1.get().isdigit() and entry2.get().isdigit():
        a = entry1.get()
        b = entry2.get()
        entry1.delete(0,END)
        entry2.delete(0, END)
        result(int(a) + int(b))

def minus():
    if entry1.get().isdigit() and entry2.get().isdigit():
        a = entry1.get()
        b = entry2.get()
        entry1.delete(0, END)
        entry2.delete(0, END)
        result(int(a) - int(b))

def multiplication():
    if entry1.get().isdigit() and entry2.get().isdigit():
        a = entry1.get()
        b = entry2.get()
        entry1.delete(0, END)
        entry2.delete(0, END)
        result(int(a) * int(b))

def division():
    if entry1.get().isdigit() and entry2.get().isdigit():
        a = entry1.get()
        b = entry2.get()
        entry1.delete(0, END)
        entry2.delete(0, END)
        result(int(a) / int(b))

def result(answer):
    if len(str(answer)) <= 21:
        result_window["text"] = answer
    else:
        result_window["text"] = "Превышен лимит"

def delete():
    if len(entry1.get()) > 20:
        entry1.delete(len(entry1.get()) - 1)
        window.update()

    if len(entry2.get()) > 20:
        entry2.delete(len(entry2.get()) - 1)
        window.update()

    window.after(10, delete)

label = Label(text="🧮Calculator🧮", font=("Arial", 20), background="turquoise", fg="blue")
label.grid()

label = Label(text="First value:", font=("Arial", 15))
label.grid(pady=20)

entry1 = Entry(window, font=("Arial", 20), background="gray75")
entry1.grid()

label = Label(text="Second value:", font=("Arial", 15))
label.grid(pady=20)

entry2 = Entry(window, font=("Arial", 20), background="gray75")
entry2.grid()

plus_button = Button(text="+", width=20, command=plus)
plus_button.grid(pady=25)

minus_button = Button(text="-", width=20, command=minus)
minus_button.grid(pady=20)

multiplication_button = Button(text="*", width=20, command=multiplication)
multiplication_button.grid(pady=20)

division_button = Button(text="/", width=20, command=division)
division_button.grid(pady=25)

result_text = Label(window, text="Result:", font=("Arial", 18))
result_text.grid()
result_window = Label(window, text="", font=("Arial", 19), background="gray80", width=20)
result_window.grid()

window.after(0, delete)
window.mainloop()