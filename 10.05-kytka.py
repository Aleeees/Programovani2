# Tento program slouží k nakreslení květiny určité barvy
from operator import contains
from tkinter import *

print("Toto je program na kreslení květin. Prosím vyberte vhodnou barvu z následující nabídky: červená, oranžová, žlutá, modrá, námořnická modrá, fialová, růžová, šedá")
vstup = input("Zadejte kód vybrané barvy: ")

# 1. Upravte kód, aby barva okvětních lístků byla určena vhodnou proměnnou
# 2. Doplňte kod, aby barva okvětních listků odpovídala volbě uživatele
#    tj. uživatel zadá česky výraz a program najde odpovidající anglický název barvy
#    Předpokládejte, že obě pole mají stejný počet prvků a že si odpovídají hodnoty na stejných indexech
#    Pokud uživatel zadá neplatný kód barvy, bude zvolena oranžová barva
# 3. Program otestujte
# 4. Do pole barvyCz přidejte za hodnotu "fialová" novou hodnotu "červená"
# 5. Do pole barvyEn přidejte za hodnotu "purple" novou hodnotu "maroon"
# 6. Program otestujte - jakou barvou bude květ vykreslen, pokud uživatel zvolí barvu "červená"?
#    O svém zjištění diskutujte se spolužákem


canvas = Canvas()
canvas.pack()

x = 150
y = 120
polomer = 30

barvyCz = ["červená", "oranžová", "žlutá", "modrá", "námořnická modrá", "fialová",'červená', "růžová", "šedá"]
barvyEn = ["red", "orange", "yellow", "blue", "navy", "purple",'maroon', "pink", "gray"]
if contains(barvyCz, vstup):
    obarvy=barvyEn[barvyCz.index(vstup)]
else:
    obarvy='orange'

canvas.create_oval(x -32-1.5*polomer, y - 32-1.5*polomer, x +32-1.5*polomer, y + 32-1.2*polomer, fill=obarvy)
canvas.create_oval(x -32+1.5*polomer, y - 32+1.5*polomer, x +32+1.5*polomer, y + 32+1.5*polomer, fill=obarvy)
canvas.create_oval(x -32-1.5*polomer, y - 32+1.5*polomer, x +32-1.5*polomer, y + 32+1.5*polomer, fill=obarvy)
canvas.create_oval(x -32+1.5*polomer, y - 32-1.5*polomer, x +32+1.5*polomer, y + 32-1.5*polomer, fill=obarvy)
canvas.create_oval(x - 40-2*polomer, y - 30, x + 40-2*polomer, y + 30, fill=obarvy)
canvas.create_oval(x - 40+2*polomer, y - 30, x + 40+2*polomer, y + 30, fill=obarvy)
canvas.create_oval(x -30, y - 40+2*polomer, x +30, y + 40+2*polomer, fill=obarvy)
canvas.create_oval(x -30, y - 40-2*polomer, x +30, y + 40-2*polomer, fill=obarvy)

canvas.create_oval(x - 32, y - 32, x + 32, y + 32, fill='orange')


mainloop()