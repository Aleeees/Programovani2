#Pět barevných čtverců leží těsně vedle sebe na jedné podložce. Velikosti stran jsou
#postupně 100, 80, 60, 40, 20. Napiš program rada_ctvercu.py, jestliže
#souřadnice levého dolního rohu prvního čtverce jsou v proměnných x, y:
#Bude program fungovat správně i v případě, že hodnotu proměnné x zvětšíš o 20
#a hodnotu proměnné y zvětšíš o 18? Jestli ne, program oprav.

from tkinter import *

x=20
y=78

create=Canvas()
create.pack()
create.create_rectangle(x,y,x+100,y+100,fill='red')
create.create_rectangle(x+100,y,x+180,y+80,fill='blue')
create.create_rectangle(x+180,y,x+240,y+60,fill='green')
create.create_rectangle(x+240,y,x+300,y+40,fill='yellow')
create.create_rectangle(x+300,y,x+320,y+20,fill='white')
mainloop()

