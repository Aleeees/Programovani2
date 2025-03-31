from tkinter import *
from random import randint as rnd



def karticky():
    create= Canvas(width=500, height=500)
    create.pack()
    for i in range(10):
        x = rnd(1,300)
        y = rnd(1,300)
        create.create_rectangle(x-30,y-70,x+30,y+70,fill="lightblue")
        create.create_text(x, y, text=i,font=("Arial",20))



karticky()
mainloop()