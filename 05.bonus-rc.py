# Toto je aplikace pro výpočet dne, měsíce a roku narození a pohlaví osoby z rodného čísla

# V současné době umí aplikace vypsat datum narození ve zkráceném tvaru, např. 25.11.98

# 1. Upravte aplikaci tak, aby uměla vypsat rok narození v nezkráceném tvaru, např. 25.11.1998
#    Pozor, rok narození může být 19xx i 20xx (předpokládejte, že RČ NEpatří osobě starší 99 let)
# 2. Aplikaci důkladně otestujte
# 3. Upravte aplikaci tak, aby uměla určit, zda se jedná o muže či ženu
# 4. Aplikaci opět otestujte


print("Toto je aplikace pro výpočet údajů z rodného čísla. Vítejte")

rcRet = input("Zadejte rodné číslo: ")

rc = int(rcRet)

zacatek = rc // 10000
den = zacatek % 100
rok = zacatek // 10000
mesic = (zacatek // 100) % 50




print(den, ".", mesic, ".", rok)
