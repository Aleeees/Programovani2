#Vytvoř program tri_soustredne.py, který nakreslí tři čtverce – všechny mají společný
#střed v bodě [x, y] a postupně se zmenšují (červený má délku stran 100, modrý 60
#a bílý 20). Předpokládej, že souřadnice x, y jsou uloženy ve stejnojmenných proměnných.
#Bude program fungovat správně i v případě, že hodnotu proměnné x zvětšíš o 17
#a hodnotu proměnné y zvětšíš o 29? Jestli ne, program oprav.

from tkinter import *

x=100
y=100

create=Canvas()
create.pack()
create.create_rectangle(x-50,y-50,x+50,y+50,fill='red')
create.create_rectangle(x-30,y-30,x+30,y+30,fill='blue')
create.create_rectangle(x-10,y-10,x+10,y+10,fill='white')
mainloop()