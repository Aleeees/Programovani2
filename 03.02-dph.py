# Tento program slouzi pro vypocet vysledne ceny za zbozi s DPH, jestlize je DPH 21 % a cena bez DPH je ziskana od uzivatele

# 1. Nejprve program otestujte, a odhalte pripadnou chybu
# 2. Promyslete, proc k teto chybe doslo, a chybu odstrante
# 3. Program znovu otestujte, zda pracuje spravne
# 4. Doplnte kod, ktery zajisti vypocet ceny zbozi vcetne DPH
# 5. Doplnte kod, ktery zajisti vypis ceny zbozi vcetne DPH
# 6. Program dukladne otestujte
# 7. Vysledny program ukazte vyucujicimu

print("Toto je aplikace pro výpočet ceny s DPH. Vítejte")
vyseDph=21
cenaRet = input("Zadejte cenu bez DPH: ")

# metoda int() zajistuje prevod retezce v promenne cenaRet na cele cislo.
# toto cislo se nasledne ulozi do promenne cena
cena = int(cenaRet)


dph = cena+(cena*(vyseDph/100))


print("DPH činí u tohoto zboží", dph, "Kč.")
