# Tato aplikace slouží ke generování dvou polí, kdy hodnoty v jednom poli jsou třikrát větší než ve druhém

# 1. Vytvořte nové pole čísel, které bude obsahovat n prvků
# 2. To tohoto nového pole vložte hodnoty, které budou třikrát větší než hodnoty v prvním poli
#    Hodnoty do druhého pole vkládejte pomocí nového cyklu, nevyužívejte k tomu stávající cyklus
#    Pokud např. budou v prvním poli hodnoty 2,7,3 pak ve druhém poli budou hodnoty 6,21,9
# 3. Obě tato pole vypište - na každém řádku bude původní číslo z prvního pole a k němu odpovídající číslo
#    z druhého pole

import random

print("Toto je aplikace pracující s náhodnými čísly. Vítejte")
n = int(input("Zadejte počet generovaných čísel: "))



prvniPole= [0]*n
druhePole=[]
for i in range(0, n):
    prvniPole[i] = random.randint(1, 100)

for i in range(0, n):
    druhePole.append(prvniPole[i]*3)
#vygenerujte pole cisel, ktera budou trikrat vetsi nez cisla v poli prvniPole
#potom obe tato pole vypiste - na kazdem radku bude puvodni cislo a k nemu cislo z noveho pole
for i in range(0,n):
    print(f'První cislo je {prvniPole[i]} a jeho nasobek 3 je {druhePole[i]}.')