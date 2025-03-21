#Chceme poslat doporučený dopis. Vytvoř program cena_dopisu.py, který ti poradí
#s cenou dopisu. Na začátku programu přiřaď do proměnné hmotnost číslo s hmotností
#tvého dopisu. Použij příkaz pro větvení programu, aby pro dopis s hmotností:
# větší než 50 vypsal Zaplatíš 55 korun,
# jinak vypsal Zaplatíš 47 korun.
#Ověř, že program počítá správně cenu dopisu pro hmotnosti: 30, 50 a 100.

hmotnost= input("Jaka je vaha dopisu: ")
hmotnost=int(hmotnost)
if hmotnost > 50:
    print("Zaplať 50Kč")
else:
    print("Zaplať 47Kč")