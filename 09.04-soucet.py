# Tato aplikace slouží k vypočítání součtu prvků pole

# 1. Pomocí libovolného cyklu spočítejte součet všech čísel v uvedeném poli
# 2. Výsledek vypište

import random

print("Toto je aplikace počítající součet prvků v poli. Vítejte")

pole = [-6, 10, -6, 1, 8, 12, 11, -3, 11, 6, 0, 10, -4, 4, 6, 14, -5, -3, -4, 10]
soucet =0
for i in range(len(pole)):
    soucet+=pole[i]
print(soucet)