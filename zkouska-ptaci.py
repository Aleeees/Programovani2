import tkinter
import random
import math

print("Toto je aplikace udržující informace o četnosti ptačích druhů")

# šířka grafického okna
sirka = 600
# výška grafického okna
vyska = 400


# Tato metoda vrací pole ptačích druhů. Do metody nemusíte zasahovat
def vratPoleDruhu():
    pozorovane = ["špaček", "sýkora", "vrabec", "kos", "vrána", "havran", "straka", "vlaštovka", "jiřička"]
    return pozorovane


# Tato metoda vrací pole četností jednotlivých ptačích druhů.
def vratPoleCetnosti():
    mnozstvi = [34, 12, 61, 25, 12, 18, 5, 9, 7]
    # 1. úkol (1 bod)
    # - Hodnoty pole: 34; 12; 61; 25; 12; 18; 5; 9; 7
    return mnozstvi


# 2. úkol (3 body) - vytvoření metody vypisDruhy
# kód metody pište sem
def vypisDruhy(druhy, cetnosti):
    for i in range(len(druhy)):
        print(druhy[i], ":", cetnosti[i], "jedinců")


# Tato metoda umožňuje uživateli vypsat pozorované ptačí druhy
# Metoda volá metodu vypisDruhy. Do kódu nemusíte zasahovat
def vypisDruhyGUI():
    vypisDruhy(vratPoleDruhu(), vratPoleCetnosti())


# 3. úkol (3 body) - vytvoření metody odmenaPozorovatele
# kód metody pište sem
def odmenaPozorovatele(jedinci):
    pocet = jedinci
    if jedinci < 13:
        pocet = jedinci * 3
    if jedinci >= 13:
        pocet = 36 + (jedinci - 12) * 2
    return pocet


# Tato metoda umožňuje uživateli zjistit odměnu za pozorování ptactva
# Metoda volá metodu odmenaPozorovatele. Do kódu nemusíte zasahovat
def odmenaPozorovateleGUI():
    pocet = int(input("Zadejte počet pozorovaných jedinců: "))
    print("Za", pocet, "pozorovaných jedinců náleží odměna", odmenaPozorovatele(pocet), "€")


# 4. úkol (3 body) - úprava metody oblibeny
def oblibeny(druhy, cetnosti):
    nahodne = random.randint(0, len(druhy) - 1)
    cetnost = cetnosti[nahodne]
    print("Náš oblíbený druh je", druhy[nahodne], ", od kterého jsme pozorovali", cetnost, "jedinců")


# Tato metoda umožňuje uživateli vypsat oblibený ptačí druh
# Metoda volá metodu oblibeny. Do kódu nemusíte zasahovat
def oblibenyGUI():
    oblibeny(vratPoleDruhu(), vratPoleCetnosti())


# 5. úkol (4 body) - úprava metody cetnostPostaru
def cetnostPostaru(desitkove):
    tucty = desitkove // 12
    kusy = desitkove % 12
    pocet = (tucty, "tuctů a ", kusy, "kusů k tomu")
    return pocet


# Tato metoda umožňuje uživateli vypsat počet pozorovaných jedinců zastaralým způsobem
# Metoda volá metodu cetnostPostaru. Do kódu nemusíte zasahovat
def cetnostPostaruGUI():
    pocet = int(input("Zadejte počet pozorovaných jedinců: "))
    print("Staročeši by řekli, že pozorovaných jedinců je", cetnostPostaru(pocet))


# 6. úkol (4 bodů) - úprava metody geometrickyPrumerCetnosti
def geometrickyPrumerCetnosti(druhy, cetnosti):
    # zde doplnte kod
    return math.sqrt(math.prod(cetnosti))


# Tato metoda umožňuje uživateli zjistit geometrický průměr četností ptačích druhů
# Metoda volá metodu geometrickyPrumerCetnosti. Do kódu nemusíte zasahovat
def geometrickyPrumerCetnostiGUI():
    prumer = geometrickyPrumerCetnosti(vratPoleDruhu(), vratPoleCetnosti())
    print("Geometrický průměr četností pozorovaných ptačích druhů je", prumer, "jedinců")


# 7. úkol (5 bodů) - optimalizace metody hranataDuha
def hranataDuha():
    canvas = tkinter.Canvas(width=sirka, height=vyska)
    canvas.pack()
    canvas.create_text(250, vyska - 20, text="Pro pokračování programu zavři toto okno", font="Arial 14")

    x = 60

    barva = ["red", "orange", "yellow", "green", "blue", "purple", "magenta"]

    for i in range(7):
        canvas.create_rectangle(x, x, 200, 200, fill=barva[i])
        x = x + 20

    canvas.mainloop()


# 8. úkol (6 bodů) - úprava metody vypisDruhyZacinajici
def vypisDruhyZacinajici(prvniPismeno, druhy):
    nalezeno=0
    for druh in druhy:
        if druh[0]==prvniPismeno:
            print(f'{druh}')
            nalezeno+=1
    if nalezeno==0:
        print(f'Nenalezen žádný ptačí druh')

# Tato metoda umožňuje uživateli vypsat ptačí druhy začínající určitým písmenem
# Metoda volá metodu vypisDruhyZacinajici. Do kódu nemusíte zasahovat
def vypisDruhyZacinajiciGUI():
    pismeno = input("Zadejte písmeno, kterým mají názvy začínat: ")
    while (len(pismeno) != 1):
        pismeno = input("Zadejte písmeno, kterým mají názvy začínat: ")
    vypisDruhyZacinajici(pismeno, vratPoleDruhu())


# 9. úkol (7 bodů) - úprava metody budky
def budky(pocet):
    canvas = tkinter.Canvas(width=sirka, height=vyska)
    canvas.pack()
    canvas.create_text(250, vyska - 20, text="Pro pokračování programu zavři toto okno", font="Arial 14")
    x=0
    y=90
    budkaSirka=35
    budkaVyska=60
    for i in range(pocet):
        if(i%2==0):
            budkaVyska=60
        else:
            budkaVyska=45
        canvas.create_rectangle(x+(i*budkaSirka),y,x+((i+1)*budkaSirka),y-budkaVyska,fill="yellow")

    canvas.mainloop()


# Tato metoda umožňuje uživateli vykreslit určitý počet ptačích budek
# Metoda volá metodu budky. Do kódu nemusíte zasahovat
def budkyGUI():
    pocet = int(input("Zadejte počet kreslených ptačích budek: "))
    budky(pocet)


# Tato metoda vypisuje informace pro uživatele
# Do kódu nemusíte zasahovat
def vypisInfo():
    print("Jakou akci chcete provést?")
    print("  2: vypisDruhy: Vypíše ptačí druhy včetně jejich četností")
    print("  3: odmenaPozorovatele: Vrátí odměnu za pozorování ptactva")
    print("  4: oblibeny: Vypíše jeden náhodně zvolený ptačí druhy")
    print("  5: cetnostPostaru: Vrátí počet pozorovaných jedinců zastaralým způsobem")
    print("  6: geometrickyPrumerCetnosti: Vrátí geometrický průměr četností ptačích druhů")
    print("  7: hranataDuha: Vykreslí hranatou duhu")
    print("  8: vypisDruhyZacinajici: Vypíše ptačí druhy začínající určitým písmenem")
    print("  9: budky: Vykreslí vedle sebe ptačí budky")
    print(" Q: Ukončit program")


# Tato metoda řídí celý program
# Do kódu nemusíte zasahovat
def zakladniSmycka():
    vypisInfo()
    klavesa = input("> ")
    if ((klavesa != "Q") and (klavesa != "q")):
        if (klavesa == "2"):
            vypisDruhyGUI()
        elif (klavesa == "3"):
            odmenaPozorovateleGUI()
        elif (klavesa == "4"):
            oblibenyGUI()
        elif (klavesa == "5"):
            cetnostPostaruGUI()
        elif (klavesa == "6"):
            geometrickyPrumerCetnostiGUI()
        elif (klavesa == "7"):
            hranataDuha()
        elif (klavesa == "8"):
            vypisDruhyZacinajiciGUI()
        elif (klavesa == "9"):
            budkyGUI()
        else:
            print("Zadaná klávesa nebyla rozpoznána. Opakujte akci...")
        print("---------------------------------")
        print("")
        zakladniSmycka()
    else:
        print("Děkujeme za použití programu")


# volání řídící metody programu
zakladniSmycka()
