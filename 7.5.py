#Vytvoř program vedle_sebe.py, který nakreslí tři vzájemně se dotýkající obdélníky:
#Souřadnice levého horního rohu prvního obdélníku jsou uložené v proměnných x, y.
#Všechny tři obdélníky mají stejnou šířku a výšku – tyto rozměry jsou uložené
#v proměnných a, b.
#Bude program fungovat správně i v případě, že hodnotu proměnné a zvětšíš o 20
#a hodnotu proměnné y zvětšíš o 10? Jestli ne, program oprav.

from tkinter import *

x=30
y=30
a=50
b=50
create= Canvas()
create.pack()
create.create_rectangle(x,y,x+a,y+b,fill='blue')
create.create_rectangle(x+a,y,x+2*a,y+b,fill='lightblue')
create.create_rectangle(x+2*a,y,x+3*a,y+b,fill='darkblue')
mainloop()