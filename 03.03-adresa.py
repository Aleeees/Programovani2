# Tento program slouzi pro vypsani adresy prijemce ve vhodnem tvaru

# 1. Pojmenujte vhodne jednotlive promenne, do kterych se maji ulozit prislusne texty
# 2. Zajistete, aby se prostrednictvim promenne adresa vypsalo do konzole jmeno a prijmeni prijemce
# 3. Program otestujte (nezadane hodnoty muzete prozatim proentrovat)
# 4. Vypiste celou adresu ve tvaru :
#       Pavel Svatek
#       Krausova 45
#       37377 Rudolfov
#    Pozn.: Pro oddeleni radku muzete vyuzit znak \n
# 5. Program otestujte


print("Toto je aplikace upožňující tisk adresy. Vítejte")

# pomoci metody input() dojde k ziskani vstupu od uzivatele
# tento vstup je posleze ulozen do prislusne promenne
promA = input("Zadejte křestní jméno: ")
promB = input("Zadejte příjmení: ")
promC = input("Zadejte město: ")
promD = input("Zadejte PSČ: ")
promE = input("Zadejte ulici: ")
promF = input("Zadejte číslo popisné: ")


adresa = (f"{promA} {promB} \n"
          f"{promE} {promF} \n"
          f"{promD} {promC}")
print(adresa)
