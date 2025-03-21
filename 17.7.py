#Do předchozího řešení doplň kreslení pozadí – měsíc se nakreslí na tmavomodré pozadí,
#slunce na světlemodré pozadí:
from tkinter import *
create= Canvas()
create.pack()

cas= input("Kolik je hodin: ")
cas= int(cas)

if cas<8:
    barva="white"
    pozadi="lightblue"
else:
    barva="yellow"
    pozadi="darkblue"

create.create_rectangle(100,0,300,200,fill=pozadi)
create.create_oval(175,75,225,125,fill=barva)


mainloop()