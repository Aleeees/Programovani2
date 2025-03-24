# Tato aplikace slouží ke zjištění, v jakém kraji se nachází daná adresa podle PSČ

# 1. Zjistěte, v jakém kraji se nachází daná adresa podle PSČ.
#    Pokud nebyla shoda nalezena, vypište "neznámém kraji"
#    - PSČ je vždy pěticiferné celé číslo, např. 37005
#    - podle první číslice lze přibližně určit kraj, ve kterém se adresa nachází
#    První číslice PSČ podle krajů:
#    1 - Praha
#    2 - Středočeský kraj
#    3 - Jihočeský nebo Západočeský kraj
#    4 - Severočeský kraj
#    5 - Východočeský kraj
#    6 - Jihomoravský kraj
#    7 - Severomoravský kraj
# 2. Program řádně otestujte pro platná i neplatná PSČ

#Pokud nebyla shoda nalezena, vypište "neznámém kraji"

print("Toto je aplikace pro zjištění adresy z PSČ v rámci ČR. Vítejte")

pscRet = input("PSČ hledané adresy: ")
psc = int(pscRet)
kraje={1:"Praha",
       2:"Středočeský kraj",
       3:"Jihočeský nebo Západočeský",
       4:"Severočeský kraj",
       5:"Východočský kraj",
       6:"Jihomoravský kraj",
       7:"Severomoravský kraj"}


print(f"Adresa se pravděpodobně nachází v {kraje[int(str(psc)[:1])]}")
