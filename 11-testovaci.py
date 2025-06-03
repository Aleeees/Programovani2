def soucet5():
    vysledek = 1+2+3+4+5
    print(vysledek)

soucet5()


def mojeMetoda1():
    vysledek = 0
    for i in range(1, 6):
        vysledek = vysledek + i
    print(vysledek)

mojeMetoda1()


import math
def soucet(a, b):
    pom = a * a + b * b
    vysledek = math.sqrt(pom)
    print(vysledek)

soucet(8, 12)



def mojeMetoda2(pole):
    nejakeCislo = pole[0]
    for i in range (0, len(pole)):
        if(nejakeCislo < pole[i]):
            nejakeCislo = pole[i]
    print(nejakeCislo)

cisla = [4,-8, 6, 1, 0, -38, 34]
mojeMetoda2(cisla)



def hledejPozici(pole, cislo):
    pozice = -1
    for i in range (0, len(pole)):
        if(cislo == pole[i]):
            pozice = i
    if(pozice>=0):
        print("Číslo", cislo, "je na indexu", pozice)
    else: print("Číslo", cislo, "se v poli nevyskytuje")

cisla = [4,-8, 6, 1, 0, -38, 4, 34]
hledejPozici(cisla, 4)
hledejPozici(cisla, 13)
