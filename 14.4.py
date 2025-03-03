#Pomocí čtverců je možné nakreslit věž z kostek. Vytvoř nový program vez.py a napiš do
#něj kód, který ji nakreslí. Při kreslení využij souřadnice z následujícího obrázku:
#[170, 50]
#[160, 90]
#[150, 150]
#[230, 230]
from tkinter import *
canvas= Canvas()
canvas.pack()
canvas.create_rectangle(170,50,210,90)
canvas.create_rectangle(160,90,220,150)
canvas.create_rectangle(150,150,230,230)



mainloop()