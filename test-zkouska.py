# TOTO JE VZOR ZKOUŠKOVÉ PÍSEMKY. POČET UVEDENÝCH ÚKOLŮ JE NIŽŠÍ NEŽ V PÍSEMCE.
# DÁLE ZDE NEJSOU UVEDENY BODY ZA SPLNĚNÍ JEDNOTLIVÝCH ÚKOLŮ

import tkinter
import random

# Tato aplikace slouží k udržování informací o nealkoholických nápojích nabízených ve stánku. Základem jsou dvě synchronizovaná pole - napoje a cenik
# Pole napoje udržuje informace o názvech nabízených nápojů
# Pole cenik udržuje informace o cenách jednotlivých nápojů z pole napoje
# Platí, že číslo na x-té pozici v poli cenik znamená cenu nápoje na x-té pozici v poli nápojů

print("Toto je aplikace udržující informace o nabízených nápojích")

# šířka grafického okna
sirka = 700
# výška grafického okna
vyska = 400

# pole nápojů
napoje = ["Pepsi", "Mirinda", "Čaj"]

# 1. úkol
# - vytvořte proměnnou cenik, která bude obsahovat pole cen jednotlivých nápojů
# - pole cenik bude obsahovat hodnoty 34, 38, 25
cenik = [34, 38, 25]


# 2. úkol
# - vytvořte metodu vypisNapoje (bez parametru), která slouží k výpisu všech nápojů a jejich cen
# - metoda bude vypisovat dvojice hodnot nápoj - cena.
# - předpokládejte, že obě pole mají stejný počet prvků a že si odpovídají hodnoty na stejných indexech
#   tj. vznikají dvojice "Pepsi: 34 Kč", "Mirinda: 38 Kč" apod.

def vypisNapoje():
    for i in range(len(napoje)):
        print(f'{napoje[i]}: {cenik[i]} Kč')


# 3. úkol
# - vytvořte metodu pocetLevnychNapoju s parametrem hranicniCena
# – metoda vrátí počet nápojů, jejichž cena je nižší než cena v parametru hranicniCena

def pocetLevnychNapoju(hranicniCena):
    levneNapoje = 0
    for i in range(len(cenik)):
        if (cenik[i] < int(hranicniCena)):
            levneNapoje += 1
    return levneNapoje


# Tato metoda umožňuje uživateli vypsat nápoje levnější než je jím zadaná hraniční cena
# Metoda volá metodu pocetLevnychNapoju. Do kódu nemusíte zasahovat

def pocetLevnychNapojuGUI():
    hranice = int(input("Zadejte maximální cenu hledaných nápojů: "))
    print("Počet nalezených nápojů je:", pocetLevnychNapoju(hranice))


# 4. úkol
# - upravte tělo metody kresliPlechovky (bez parametru) uvedené níže
#   metoda bude kreslit vedle sebe střídavě velké a malé obdélníky (představující plechovky) tak, aby jich bylo celkem 18
#   * každý obdélník bude mít šířku 33
#   * vyšší obdélník bude mít výšku 40, nižší obdélník bude mít výšku 30
# - první obdélník bude u levého okraje okna
# - barva výplně obdélníků bude světle šedá
# - VZOR: Vzorové výsledek naleznete v souboru nealkoNapoje-vzory.docx
def kresliPlechovky():
    canvas = tkinter.Canvas(width=sirka, height=vyska)
    canvas.pack()
    canvas.create_text(250, vyska - 20, text="Pro pokračování programu zavři toto okno", font="Arial 14")
    x=0
    y=60
    obdelnikSirka=33
    obdelnikVyska=30
    for i in range(18):
        if i%2==0:
            obdelnikVyska=40
        else:
            obdelnikVyska=30
        canvas.create_rectangle(x+(i*obdelnikSirka),y-obdelnikVyska,x+((i+1)*obdelnikSirka),y,fill="lightgray")

    canvas.mainloop()


# Tato metoda vypisuje informace pro uživatele
# Do kódu nemusíte zasahovat
def vypisInfo():
    print("Jakou akci chcete provést?")
    print(" 2: vypisNapoje: Výpis všech nápojů a jejich cen")
    print(" 3: pocetLevnychNapoju: Počet nápojů, jejichž cena je nižší než zvolená hranice")
    print(" 4: kresliPlechovky: Vykreslí na plátno plechovky přes celou šířku plátna")
    print(" Q: Ukončit program")


# Tato metoda řídí celý program
# Do kódu nemusíte zasahovat
def zakladniSmycka():
    vypisInfo()
    klavesa = input("> ")
    if ((klavesa != "Q") and (klavesa != "q")):
        if (klavesa == "2"):
            vypisNapoje()
        elif (klavesa == "3"):
            pocetLevnychNapojuGUI()
        elif (klavesa == "4"):
            kresliPlechovky()
        else:
            print("Zadaná klávesa nebyla rozpoznána. Opakujte akci...")
        print("---------------------------------")
        print("")
        zakladniSmycka()
    else:
        print("Děkujeme za použití programu")


# volání řídící metody programu
zakladniSmycka()











