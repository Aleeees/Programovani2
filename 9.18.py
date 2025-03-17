#Vytvoř nový program sportovni_vlajka.py, který bude kreslit sportovní vlajku vaší
#třídy. Vlajka bude tvořena čtyřmi barevnými obdélníky, které se vzájemně dotýkají
#v jediném bodě jako na obrázku níže:
#Program si náhodně zvolí souřadnice x, y, které představují místo dotyku všech čtyř
#obdélníků. Vnější rozměry vlajky nechť jsou 300x200; barvy na vlajce si urči podle svého
#uvážení.

from tkinter import *
import random as rn
x= rn.randint(10,290)


canvas= Canvas()
canvas.pack()
canvas.create_rectangle(0,0,x,100,fill="white")
canvas.create_rectangle(x,0,300,100,fill="blue")
canvas.create_rectangle(0,100,x,200,fill="green")
canvas.create_rectangle(x,100,300,200,fill="red")


mainloop()
