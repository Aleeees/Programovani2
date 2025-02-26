#Vytvoř program vedle_sebe.py, který nakreslí tři vzájemně se dotýkající obdélníky:
#Souřadnice levého horního rohu prvního obdélníku jsou uložené v proměnných x, y.
#Všechny tři obdélníky mají stejnou šířku a výšku – tyto rozměry jsou uložené
#v proměnných a, b.
#Bude program fungovat správně i v případě, že hodnotu proměnné a zvětšíš o 20
#a hodnotu proměnné y zvětšíš o 10? Jestli ne, program oprav.

from tkinter import *

x=30
y=30

create= Canvas()
create.pack()
create.create_rectangle(x,y,x+50,y+50,fill='blue')
create.create_rectangle(x+50,y,x+100,y+50,fill='lightblue')
create.create_rectangle(x+100,y,x+150,y+50,fill='darkblue')
mainloop()