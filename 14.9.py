#Diskutuj se sousedem, jak nakreslit kruh, jestliže znáš jeho střed a poloměr. Potom vytvoř
#nový program znacka.py, který pomocí příkazu canvas.create_oval nakreslí
#dopravní značku Zákaz vjezdu (viz obrázek níže). Značka bude tvořena dvěma
#soustřednými kruhy, jejichž společný střed bude mít souřadnice [200, 100]. Velký
#červený kruh bude mít poloměr 45 a bílý kruh bude mít poloměr 35.

from tkinter import *
canvas= Canvas()
canvas.pack()
x=200
y=100
canvas.create_oval(x+45,y+45,x-45,y-45,fill="red")
canvas.create_oval(x+35,y+35,x-35,y-35,fill="white")

mainloop()