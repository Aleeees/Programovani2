# Toto je aplikace na výpočet ceny počítačové sestavy vč. příslušenství

# 1. Upravte kód tak, aby v případě, že chce klávesnici, byla cena sestavy zvýšena o 100 Kč
# 2. Upravte kód tak, aby v případě, že chce myš, byla cena sestavy zvýšena o 200 Kč
# 3. Aplikaci otestujte
# 4. Upravte kód tak, aby v případě, že chce klávesnici, byl dotázán, zda chce drátovou nebo bezdrátovou.
#    Následně bude podle jeho volby zvýšena cena celé sestavy:
#    -  Pokud chce drátovou, bude cena sestavy zvýšena o 100 Kč
#    -  Pokud chce bezdrátovou, bude cena sestavy zvýšena o 300 Kč
# 5. Aplikaci otestujte
# 4. Upravte kód tak, aby v případě, že chce myš, byl dotázán, zda chce drátovou nebo bezdrátovou.
#    Následně bude podle jeho volby zvýšena cena celé sestavy:
#    -  Pokud chce drátovou, bude cena sestavy zvýšena o 200 Kč
#    -  Pokud chce bezdrátovou, bude cena sestavy zvýšena o 400 Kč
# 5. Aplikaci otestujte
#    - klávesnice: ne,               myš: ne               -> cena se zvýší o   0 Kč
#    - klávesnice: ano - bezdrátová, myš: ano - bezdrátová -> cena se zvýší o 700 Kč
#    - klávesnice: ano - drátová,    myš: ano - drátová    -> cena se zvýší o 300 Kč
#    - klávesnice: ne,               myš: ano - drátová    -> cena se zvýší o 200 Kč
#    - klávesnice: ano - bezdrátová, myš: ne               -> cena se zvýší o 300 Kč

import random

print("Toto je aplikace pro výpočet ceny počítačové sestavy. Vítejte")
cena = random.randint(8000, 30000)
print("Cena sestavy bez příslušenství je "+str(cena)+" Kč.")

klavesnice = input("Chcete zakoupit klávesnici? (ano / ne): ")


mys = input("Chcete zakoupit myš? (ano / ne): ")



vyslednaCena = 0

print("Výsledná cena sestavy bude", vyslednaCena, "Kč")

