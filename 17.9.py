#Vylepši předchozí program tak, aby fungoval jako náhodný generátor krajinek – přiřaď na
#začátku do proměnných x, y, cas náhodná čísla:
# x z rozsahu 100, 300
# y z rozsahu 100, 200
# cas z rozsahu 0, 16
#Program několikrát spusť a sleduj, zda se krajinky vytváří dle tvého očekávání:

from tkinter import *
import random as rnd
create= Canvas()
create.pack()

cas=rnd.randint(0,16)
x=rnd.randint(100,300)
y=rnd.randint(100,200)
if cas<8:
    barva="white"
    pozadi="lightblue"
if cas==4:
    x=200
    y=150
if cas==14:
    x=200
    y=150
else:
    barva="yellow"
    pozadi="darkblue"

create.create_rectangle(100,0,400,200,fill=pozadi)
create.create_oval(x-25,y-25,x+25,y+25,fill=barva)
create.create_rectangle(100,150,400,200,fill="green")



mainloop()