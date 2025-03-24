# Tento program slouzi pro vypsani adresy prijemce ve vhodnem tvaru
# Výpis adresy bude včetně oslovení příjemce ve tvaru:
#    Vážený pan
#    Pavel Svatek
#    Krausova 45
#    37377 Rudolfov

# 1. Na základě hodnoty proměnné pohlavi vypište oslovení "Vážený pan" nebo "Vážená paní"
#    Předpokládejte, že uživatel jako pohlaví zadává "muž" nebo "žena" 
# 2. Program otestujte pro zadané pohlaví "muž"; "žena"; "muuž", "žeena"
# 3. Upravte program, aby v případě zkomoleného pohlaví nevypsal oslovení žádné
# 4. Program otestujte pro zadané pohlaví "muž"; "žena"; "muuž", "žeena"
# 5. Upravte program, aby vypsal správné oslovení pro pohlaví "muž" i "Muž", "žena" i "Žena"
# 6. Program opět důkladně otestujte


print("Toto je aplikace upožňující tisk adresy. Vítejte")

pohlavi = input("Zadejte pohlaví příjemce (muž / žena): ")
jmeno = input("Zadejte křestní jméno: ")
prijmeni = input("Zadejte příjmení: ")
mesto = input("Zadejte město: ")
psc = input("Zadejte PSČ: ")
ulice = input("Zadejte ulici: ")
cp = input("Zadejte číslo popisné: ")


pohlavi=pohlavi.lower()
if(pohlavi=="muž"):
    osloveni="Vážený pane"
elif(pohlavi=="žena"):
    osloveni="Vážená paní"
else:
    osloveni=""
adresa =osloveni+"\n" + jmeno+" "+prijmeni+"\n"+ulice+" "+cp+"\n"+psc+" "+mesto
print(adresa)
