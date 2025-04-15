from tkinter import *


def pyramida(pocet):
    canvas=Canvas()
    canvas.pack()
    x=canvas.winfo_width()+200
    y=10
    for i in range(pocet):
        canvas.create_rectangle((x/2)-(i*10),y,(x/2)+(i*10),y+20,fill="yellow")
        y+=20

pyramida(5)
mainloop()