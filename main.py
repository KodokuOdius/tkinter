import keyword
from tkinter import *
import random


def do():
    try:
        val = int(enter_box.get())
        lable_answer_box["text"] = f"{(val - 32) * 5 / 9}"
    except ValueError:
        lable_answer_box["text"] = "None"



window = Tk()
window.title("Practical")
window.resizable(False, False)

window.rowconfigure(0, minsize=50, weight=1)
window.columnconfigure([0, 1], minsize=50, weight=1)

enter_frame = Frame(master=window)
enter_box = Entry(
    master=enter_frame,
    width=10
)
lable_enter_box1 = Label(
    master=enter_frame,
    text="F"
)
enter_box.grid(row=0, column=0, sticky="e")
lable_enter_box1.grid(row=0, column=1, sticky="w")


answer_frame = Frame(master=window)
button_box = Button(
    master=answer_frame,
    text="->",
    command=do
)
lable_answer_box = Label(
    master=answer_frame,
    text="None"
)
lable = Label(
    master=answer_frame,
    text="C"
)
button_box.grid(row=0, column=0, sticky="e")
lable_answer_box.grid(row=0, column=1)
lable.grid(row=0, column=2, sticky="w")


enter_frame.grid(row=0, column=0, sticky="w")
answer_frame.grid(row=0, column=1, sticky="e")


def handle_keypress(event):
    if event.char == "":
        do()

window.bind("<Key>", handle_keypress)

window.mainloop()
