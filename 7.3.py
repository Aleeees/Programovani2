#Vytvoř nový program obdelnik_promenne.py, který použije čtyři proměnné x, y,
#sirka, vyska a na jejich základě nakreslí obdélník s levým horním rohem na
#souřadnicích x, y, danou šířkou a výškou. Barvu si zvol podle svého. Například když bude v programu:

from tkinter import *
x = 100
y = 70
sirka = 200
vyska = 50

create=Canvas()
create.pack()
create.create_rectangle(x, y, x+sirka,y+vyska,fill="red")
mainloop()