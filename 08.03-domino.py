#Víte, jak vypadá padající had z domina? Vytvořte program domino.py, který pomocí cyklu a obdélníku nakreslí zatím ještě stojící kostky domina jako na obrázku níže. Počet kostek domina nechť je uložen v proměnné pocet.

from tkinter import *



def domino(pocet):
    canvas=Canvas()
    canvas.pack()
    x=10
    for i in range(pocet):
        canvas.create_rectangle(x,10,x+10,50,fill="red")
        x+=20


domino(5)
mainloop()