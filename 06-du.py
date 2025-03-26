from tkinter import *
canvas = Canvas()
canvas.pack()
def semafor(canvas,cas):
    if cas<28:
        canvas.create_oval(100, 80, 160, 140, fill="red")
        canvas.create_oval(100, 200, 160, 260)
        canvas.create_oval(100, 140, 160, 200)
        #vykresli červenou
    elif cas>32:
        canvas.create_oval(100, 140, 160, 200)
        canvas.create_oval(100, 80, 160, 140)
        canvas.create_oval(100, 200, 160, 260, fill="green")
        #vykresli zelenou
    elif cas>=28 and cas<32:
        canvas.create_oval(100, 200, 160, 260)
        canvas.create_oval(100, 140, 160, 200, fill="orange")
        canvas.create_oval(100, 80, 160, 140)
        #oranžová


semafor(canvas,50)

mainloop()