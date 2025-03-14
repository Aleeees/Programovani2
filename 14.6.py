#Napiš program ufo.py, který pomocí alespoň pěti elips nakreslí UFO. Rozměry i barvy
#zvol dle svého uvážení. Inspirovat se můžeš (ale nemusíš) na následujícím obrázku:
#Barevné elipsy se kreslí podobně jako barevné obdélníky pomocí parametru fill:
#canvas.create_oval(x1, y1, x2, y2, fill='barva')

from tkinter import *
canvas= Canvas()
canvas.pack()
canvas.create_oval(130,70,220,150,fill="gray")
canvas.create_oval(100,100,250,150,fill="gray")
canvas.create_oval(130,120,140,130,fill="blue")
canvas.create_oval(170,120,180,130,fill="green")
canvas.create_oval(210,120,220,130,fill="yellow")



mainloop()