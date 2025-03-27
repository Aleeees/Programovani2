# Tento program slouží k nakreslení květiny určité barvy
from tkinter import *

print("Toto je program na kreslení květin. Prosím vyberte vhodnou barvu z následující nabídky:\n1: červená\n2: žlutá\n3: modrá\n4: oranžová\n5: šedá")
vstup = input("Zadejte kód vybrané barvy: ")

#1. Upravte kod, aby barva okvětních lístků byla určena vhodnou proměnnou
#2. Doplnte kod, aby se barva okvetnich listku odpovidala volbe uzivatele
#   Pokud uživatel zadá neplatný kód barvy, bude zvolena červená barva
#3. Program důkladně otestujte

if vstup == "1":
    barva="red"
elif vstup == "2":
    barva="yellow"
elif vstup == "3":
    barva="barva"
elif vstup == "4":
    barva="orange"
elif vstup == "5":
    barva="gray"
else:
    barva="red"

canvas = Canvas()
canvas.pack()

x = 150
y = 120
polomer = 30

canvas.create_oval(x -32-1.5*polomer, y - 32-1.5*polomer, x +32-1.5*polomer, y + 32-1.2*polomer, fill=barva)
canvas.create_oval(x -32+1.5*polomer, y - 32+1.5*polomer, x +32+1.5*polomer, y + 32+1.5*polomer, fill=barva)
canvas.create_oval(x -32-1.5*polomer, y - 32+1.5*polomer, x +32-1.5*polomer, y + 32+1.5*polomer, fill=barva)
canvas.create_oval(x -32+1.5*polomer, y - 32-1.5*polomer, x +32+1.5*polomer, y + 32-1.5*polomer, fill=barva)
canvas.create_oval(x - 40-2*polomer, y - 30, x + 40-2*polomer, y + 30, fill=barva)
canvas.create_oval(x - 40+2*polomer, y - 30, x + 40+2*polomer, y + 30, fill=barva)
canvas.create_oval(x -30, y - 40+2*polomer, x +30, y + 40+2*polomer, fill=barva)
canvas.create_oval(x -30, y - 40-2*polomer, x +30, y + 40-2*polomer, fill=barva)

canvas.create_oval(x - 32, y - 32, x + 32, y + 32, fill='orange')


mainloop()