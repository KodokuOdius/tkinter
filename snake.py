
from tkinter import *

"""
    !!!!!!!!!!!!!!!!!!!!!!!
        ЖРЁТ ПАМЯТЬ
        ЖДЁТ ОПЕРАТИВКУ
        ЖРЁТ ЛЮБИМУЮ RAM
        ИСПРАВИТЬ
    !!!!!!!!!!!!!!!!!!!!!!!
"""



window = Tk()
window.title("Practical")
window.resizable(False, False)
window["bg"] = "black"
fieldX = 25
fieldY = 25
i = 0
listX = []
while i != fieldX:
    listX.append(i)
    i += 1
i = 0
listY = []
while i != fieldX:
    listY.append(i)
    i += 1


window.rowconfigure(listX, minsize=10, weight=1)
window.columnconfigure(listY, minsize=10, weight=1)

i = 0
while i != fieldX:
    j = 0
    while j != fieldY:
        Label(
            master=window,
            bg="black",
            relief="ridge",
            width = 2
        ).grid(row=i, column=j, sticky="swen")
        j += 1
    i += 1


headX = fieldX//2
headY = fieldY//2 
Label(
    master=window,
    bg="green",
    relief="ridge",
    width = 2
).grid(row=headX, column=headY, sticky="swen")

def move_up():
    global headX
    if headX != 0:
        Label(
            master=window,
            bg="black",
            relief="ridge",
            width = 2
        ).grid(row=headX, column=headY, sticky="swen")
        headX -= 1
        Label(
            master=window,
            bg="green",
            relief="ridge",
            width = 2
        ).grid(row=headX, column=headY, sticky="swen")

def move_down():
    global headX
    if headX != fieldX - 1:
        Label(
            master=window,
            bg="black",
            relief="ridge",
            width = 2
        ).grid(row=headX, column=headY, sticky="swen")
        headX += 1
        Label(
            master=window,
            bg="green",
            relief="ridge",
            width = 2
        ).grid(row=headX, column=headY, sticky="swen")

def move_left():
    global headY
    if headY != 0:
        Label(
            master=window,
            bg="black",
            relief="ridge",
            width = 2
        ).grid(row=headX, column=headY, sticky="swen")
        headY -= 1
        Label(
            master=window,
            bg="green",
            relief="ridge",
            width = 2
        ).grid(row=headX, column=headY, sticky="swen")

def move_right():
    global headY
    if headY != fieldY - 1:
        Label(
            master=window,
            bg="black",
            relief="ridge",
            width = 2
        ).grid(row=headX, column=headY, sticky="swen")
        headY += 1
        Label(
            master=window,
            bg="green",
            relief="ridge",
            width = 2
        ).grid(row=headX, column=headY, sticky="swen")


def handle_keypress(event):
    if event.char == "w":
        move_up()
    elif event.char == "a":
        move_left()
    elif event.char == "s":
        move_down()
    elif event.char == "d":
        move_right()
    elif event.char == "x":
        window.destroy

    
    

window.bind("<Key>", handle_keypress)

window.mainloop()
