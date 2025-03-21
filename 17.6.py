#Vytvoř program den_noc.py, který podle zadaného času nakreslí do grafické plochy
#slunce nebo měsíc. Do proměnné cas přiřaď počet hodin. Použij příkaz větvení na to,
#aby se pro cas < 8 kreslil měsíc jako bílý kruh, jinak se kreslilo slunce jako žlutý kruh.
#Poloměr kruhu nechť je v obou případech 50 a střed kruhu má souřadnice [200, 100].
#Program by měl například nakreslit:
from tkinter import *
create= Canvas()
create.pack()

cas= input("Kolik je hodin: ")
cas= int(cas)

if cas<8:
    barva="white"
else:
    barva="yellow"

create.create_oval(175,75,225,125,fill=barva)


mainloop()