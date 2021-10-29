import random
from tkinter import *

"""
    !!!!!!!!!!!!!!!!!!!!!!!
        ДОБАВИТЬ ЛОГИКУ НЕПРЕРЫВНОГО ДВИЖЕНИЯ
        ШОБЫ ДВИГАЛОСЬ
        НУ ТЫ ПОНЯЛ 
        А ЕЩЁ ЛОГИКУ УДЛИНЕНИЯ
        ИСПРАВИТЬ
    !!!!!!!!!!!!!!!!!!!!!!!
"""



window = Tk()
window.title("Snakei I")
window.resizable(False, False)
window["bg"] = "black"
fieldX = 11
fieldY = 11
listX = []
listY = []
for i in range(fieldX):
    listX.append(i)
    for j in range(fieldY):
        listY.append(i)

window.rowconfigure(listX, minsize=10, weight=1)
window.columnconfigure(listY, minsize=10, weight=1)

del listX
del listY 

Field = []
temp_field = []

for i in range(fieldX):
    for j in range(fieldY):
        temp_field.append(Label(
            master=window,
            bg="black",
            # relief="ridge",
            width = 2
        ))
        temp_field[j].grid(row=i, column=j, sticky="swen")
    Field.append(temp_field)
    temp_field = []

del temp_field
headX = fieldX//2
headY = fieldY//2

Field[headX][headY]["bg"] = "green"

appleX = random.randint(0, fieldX - 1)
appleY = random.randint(0, fieldY - 1)
while appleX == headX and appleY == headY:
    appleX = random.randint(0, fieldX - 1)
    appleY = random.randint(0, fieldY - 1)
Field[appleX][appleY]["bg"] = "red"

def move_up():
    global headX
    if headX != 0:
        Field[headX][headY]["bg"] = "black"
        headX -= 1
        Field[headX][headY]["bg"] = "green"

def move_down():
    global headX
    if headX != fieldX - 1:
        Field[headX][headY]["bg"] = "black"
        headX += 1
        Field[headX][headY]["bg"] = "green"

def move_left():
    global headY
    if headY != 0:
        Field[headX][headY]["bg"] = "black"
        headY -= 1
        Field[headX][headY]["bg"] = "green"

def move_right():
    global headY
    if headY != fieldY - 1:
        Field[headX][headY]["bg"] = "black"
        headY += 1
        Field[headX][headY]["bg"] = "green"


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
        exit()

    
    

window.bind("<Key>", handle_keypress)

window.mainloop()
