from tkinter import *
import random


def koralky1(canvas):
    x=20
    vykresli=1
    barva={1:"red",2:"blue"}
    for i in range(15):
        canvas.create_oval(x, 20,x+20, 40, fill=barva[vykresli])
        if i>=7:
            vykresli=2
        x+=20

def koralky2(canvas):
    x=20
    vykresli=1
    prvni=['red','yellow','silver','purple']
    for i in range(15):
        if i>=7:
            barva="blue"
        else:
            barva=random.choice(prvni)
        canvas.create_oval(x, 20,x+20, 40, fill=barva)
        x+=20


def koralky3(canvas):
        x = 20
        vykresli = 1
        prvni = ['red', 'yellow', 'silver', 'purple']
        druhy=['blue','green','black']
        for i in range(15):
            if i >= 7:
                barva = random.choice(druhy)
            else:
                barva = random.choice(prvni)
            canvas.create_oval(x, 20, x + 20, 40, fill=barva)
            x += 20


canvas= Canvas()
canvas.pack()


#koralky1(canvas)
#koralky2(canvas)
koralky3(canvas)
mainloop()