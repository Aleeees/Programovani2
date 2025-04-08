from tkinter import *
from random import randint as rnd
def zlatokop():
    canvas=Canvas()
    canvas.pack()
    x= 50
    y= 100
    for i in range(10):
        cislo=rnd(10,41)
        canvas.create_rectangle(x,y,x+cislo,y-cislo,fill="gold")
        x+=cislo

def zlatokopMezery():
    canvas = Canvas()
    canvas.pack()
    x = 50
    y = 100
    for i in range(10):
        cislo = rnd(10, 41)
        canvas.create_rectangle(x, y, x + cislo, y - cislo, fill="gold")
        x += cislo+5


zlatokop()
zlatokopMezery()
mainloop()