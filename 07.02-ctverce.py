from tkinter import *
import random as rnd

def kresliCtverce():
    create=Canvas()
    create.pack()
    for i in range(1,2001):
        x=rnd.randint(1,300)
        y=rnd.randint(1,300)
        if i%2==0:
            create.create_rectangle(x,y,x+10,y+10,fill="red")
        else:
            create.create_rectangle(x, y, x + 10, y + 10, fill="blue")


def kresliViceCtvercu():
    create=Canvas()
    create.pack()
    for i in range(1,2001):
        x=rnd.randint(1,300)
        y=rnd.randint(1,300)
        create.create_rectangle(x, y, x + 10, y + 10, fill="red")
    for i in range(1,2001):
        x=rnd.randint(1,300)
        y=rnd.randint(1,300)
        create.create_rectangle(x, y, x + 10, y + 10, fill="blue")


kresliCtverce()
kresliViceCtvercu()
mainloop()