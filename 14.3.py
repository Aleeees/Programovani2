#Přidej na konec programu příkaz pro kreslení obdélníku se stejnými čísly, jako jsou
#v příkazu create_oval. Jaká bude vzájemná pozice elipsy a obdélníku?
#Čísla, která píšeme do závorek v příkazech canvas.create_oval
#a canvas.create_rectangle, nazýváme parametry:
#canvas.create_rectangle(x1, y1, x2, y2)
#canvas.create_oval(x1, y1, x2, y2)
#V příkazu create_rectangle určovaly dvojice [x1, y1], [x2, y2] souřadnice
#protilehlých vrcholů kresleného obdélníku. V příkazu create_oval určují dvojice
#[x1, y1], [x2, y2] souřadnice protilehlých vrcholů obdélníku, do kterého se vepíše
#elipsa. Obdélník se však nenakreslí.

from tkinter import *
create=Canvas()
create.pack()
x1=50
x2=100
y1=50
y2=100
create.create_rectangle(x1, y1, x2, y2, fill="red")
create.create_oval(x1, y1, x2, y2, fill="yellow")
mainloop()