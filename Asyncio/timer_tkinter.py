import time
import tkinter

def seconds():
    start_time = time.time()
    while True:
        yield round(time.time() - start_time)

def update_seconds():
    time_label["text"] = next(s)
    window.after(50, update_seconds)

s = seconds()

window = tkinter.Tk()
window.geometry("500x500")

time_label = tkinter.Label(window, text=0, font=("Arial", 20))
time_label.pack()

window.after(0, update_seconds)
window.mainloop()