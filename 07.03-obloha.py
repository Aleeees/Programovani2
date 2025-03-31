from tkinter import *
from random import randint as rnd


def obloha():
    create=Canvas()
    create.pack()
    create.create_rectangle(0,0,300,300,fill="blue")
    for i in range(1000):
        x=rnd(1,296)
        y=rnd(1,296)
        velikost=rnd(2,4)
        create.create_rectangle(x,y,x+velikost,y+velikost,fill="yellow")


obloha()
mainloop()