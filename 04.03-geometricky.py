# Tento program slouzi k vypoctu geometrickeho prumeru dvou cisel
from cmath import sqrt

from Cviceni1 import vydel
# 1. V souboru vzorce.docx naleznete vzorec, pomoci ktereho prumer spocitate
# 2. Doplnte na vhodne misto v kodu potrebny vypocet
# 3. Program dukladne otestujte 
# 4. Diskutujte se sousedem, pro ktera cela cisla program "pada"
import math

print("Toto je aplikace pro výpočet geometrického průměru dvou čísel. Vítejte")

aRet = input("Zadejte první číslo: ")
bRet = input("Zadejte druhé číslo: ")
a = float(aRet)
b = float(bRet)

# zde doplnte potrebny kod
vysledek = sqrt(a*b)

print(vysledek)
