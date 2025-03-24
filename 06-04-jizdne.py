# Tato aplikace slouží k výpočtu ceny jízdného s přihlédnutím k možným slevám 

#1. Zajistěte výpočet výsledné ceny jízdného, jestliže uživatel zadává
#   cenu základního jízdného. Dále pomocí ano / ne zadává, zda chce
#   daný typ slevy (viz dále).
#   Při zakoupení zpáteční jízdenky je cena o 5 % nižší
#      než cena DVOU jednosměrných jízdenek
#   Při uplatnění studentské slevy je cena o 40 % nižší
#      než cena základní jízdenky
#   Slevy lze kombinovat
#   Pozor, uživatel může zadat "ano" i "Ano" nebo "ANO" (obdobně pro zápornou odpověď).

#2. Výsledný program řádně otestujte.
#   Při testování využijte mmj. následující testovací sady:
#   - cena=100; zpatecni=ne;  student=ne  -> výsledná cena: 100 Kč
#   - cena=100; zpatecni=ano; student=ne  -> výsledná cena: 190 Kč
#   - cena=100; zpatecni=ne;  student=ano -> výsledná cena: 60 Kč
#   - cena=100; zpatecni=ano; student=ano -> výsledná cena: 114 Kč
def cenaJizdneho(cena,zpatecni,student):
    print("Toto je aplikace pro výpočet slevy na jízdném. Vítejte")

    #cenaRet = input("Zadejte cenu jízdného bez slevy: ")
    cena = int(cena)
    #zpatecni = input("Chcete zakoupit zpáteční jízdenku? (ano / ne): ")
    #student = input("Chcete uplatnit studentskou slevu? (ano / ne): ")
    zpatecni = zpatecni.lower()
    student = student.lower()
    if zpatecni=="ano":
        cena=cena*2
        zpatecniSleva=(cena/100)*5
    else:
        zpatecniSleva=0
    if student=="ano":
        studentSleva=(cena/100)*40
    else :
        studentSleva=0
    vyslednaCena = cena-zpatecniSleva-studentSleva

    print("Výsledná cena jízdenky bude", vyslednaCena, "Kč")

cenaJizdneho(100,"ne","ne")
cenaJizdneho(100,"ano","ne")
cenaJizdneho(100,"ne","ano")
cenaJizdneho(100,"ano","ano")