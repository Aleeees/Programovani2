# Tato aplikace slouží ke zjištění největšího prvku v poli
from contextlib import nullcontext

# 1. Zamyslete se nad algoritmem, jak zjistit největší hodnotu z množiny nějakých čísel
#    Pokud tvrdíte, že kouknete a vidíte, zamyslete se, jak určíte největší číslo
#    promítané v programu 06-toJeVidet.py
# 2. Za použití cyklu zjistěte největší prvek v poli pole
#    Použití metody max je zakázáno!
#    Jestli si nevíte rady, požádejte o pomoc vyučujícího
# 3. Největší prvek v poli vypište
# 4. Zakomentujte řádek pole = [80, ... a odkomentujte řádek pole = [-10, ...
# 5. Otestujte, zda bude program fungovat správně i v případě tohoto druhého pole čísel



print("Toto je aplikace zjišťující maximální prvek v poli. Vítejte")


pole = [80, 54, 16, 54, 99, 53, 69, 87, 93, 80, 37, 24, 79, 68, 69, 10, 99, 7, 4, 68]

#pole = [-10, -54, -16, -54, -99, -53, -69, -87, -93, -80, -37, -24, -79, -68, -69, -10, -99, -7, -41, -68]
nejvetsi=pole[0]
for i in range(len(pole)):
    if nejvetsi<pole[i]:
        nejvetsi=pole[i]
print(nejvetsi)
