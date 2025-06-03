from tkinter import *
from random import randint as rnd


def dlazebni_kostka():
    canvas=Canvas(width=800, height=600)
    canvas.pack()
    x=10
    for i in range(20):
        space = rnd(12, 20)
        canvas.create_rectangle(x*i+space,10,(x*i)+10,20,fill="gray")





dlazebni_kostka()
mainloop()
