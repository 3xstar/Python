from tkinter import *
import json

def write_json(file_name, data):
    with open(file_name, "w+", encoding="utf-8") as file:
        json.dump(data, file, indent=2)

def read_json(file_name):
    with open(file_name, "r+", encoding="utf-8") as file:
        return json.load(file)

def listbox_to_dict():
    count = listbox.size()
    elements = listbox.get(0, END)
    data = {}
    for i in range(count):
        data[i] = elements[i]
    return data

def add_task():
    count = listbox.size()
    task = entry.get()
    if task:
        listbox.insert(END, f"{count+1}. {task}")
        entry.delete(0, END)

        data = listbox_to_dict()
        write_json("data.json", data)

def delete_task():
    selected = listbox.curselection()
    if selected:
        listbox.delete(selected)

    window.update()
    count = listbox.size()
    elements = listbox.get(0, END)

    listbox.delete(0, END)
    for i in range(count):
        listbox.insert(END, f"{i + 1}. {elements[i][3:len(elements[i])]}")

    data = listbox_to_dict()
    write_json("data.json", data)


window = Tk()
window.title("Tasks")
window.geometry("300x500")

listbox = Listbox(window, height=20, font=("Arial", 13),
                  highlightcolor="blue", selectbackground="gray", fg="black")
listbox.pack(fill=BOTH)

data = read_json("data.json")
if data:
    for element in data.values():
        listbox.insert(END, element)

entry = Entry(window, font=("Arial", 20))
entry.pack(fill=X, padx=20)

add_button = Button(window, text="Add task", width=10, command=add_task)
add_button.pack()

del_button = Button(window, text="Delete task", width=10, command=delete_task)
del_button.pack()


window.mainloop()