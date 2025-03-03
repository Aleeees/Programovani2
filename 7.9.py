#Zkus (podobně jako v úloze 6) vymyslet kreslení obdélníku, jehož střed má souřadnice
#[x, y] a strany mají délky a, b. Napiš program stred_obdelniku.py, který
#takový obdélník nakreslí.

from tkinter import *

x=100
y=200

a=100
b=200

create=Canvas()
create.pack()
create.create_rectangle(x-a/2,y-b/2,x+a/2,y+b/2,fill='green')
mainloop()