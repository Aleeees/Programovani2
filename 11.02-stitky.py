from tkinter import *
import random as rn
def stitek(x,y,jmeno):
    canvas=Canvas()
    canvas.pack()
    canvas.create_rectangle(x-25,y-10,x+25,y+10,fill="white")
    canvas.create_text(x,y,text=jmeno)


for i in range(0,100):
    poloha=rn.randint(30,200)
    stitek(poloha,poloha,i)



mainloop()