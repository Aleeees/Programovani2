# Tento program slouží ke zjištění, zda je rodné číslo platné
# Rodné číslo je platné, pokud je dělitelné 11 beze zbytku (tj. zbytek je 0)

# 1. Zajistěte kontrolu, zda je rodné číslo platné, nebo ne, 
#    a vypište o tom patřičnou informaci
#    Text "Díky za použití našeho programu" se vypíše vždy
# 2. Program otestujte pro platná i neplatná rodná čísla
#    Pokud Vás nenapadá žádné neplatné RČ, poraďte se s učitelem



print("Toto je program na kontrolu platnosti rodného čísla. Vítejte")
rcRet = input("Zadejte rodné číslo: ")
rc = int(rcRet)


if rc%11!=0:
    print("Zatím nedokážu rozhodnout :(")
else:
    print(f"Rodné číslo {rc} je platné")
print("Díky za použití našeho programu")
