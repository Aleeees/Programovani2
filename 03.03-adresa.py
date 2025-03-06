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
jmeno = input("Zadejte křestní jméno: ")
prijmeni = input("Zadejte příjmení: ")
Mesto = input("Zadejte město: ")
PSC = input("Zadejte PSČ: ")
Ulice = input("Zadejte ulici: ")
PopisneCislo = input("Zadejte číslo popisné: ")


adresa = (f"{jmeno} {prijmeni} \n"
          f"{Ulice} {PopisneCislo} \n"
          f"{PSC} {Mesto}")
print(adresa)
