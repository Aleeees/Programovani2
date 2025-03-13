#Internetový obchod s hudbou nabízí 20% slevu. Chceš si koupit album, jehož původní cena
#byla 199 korun. Napiš program sleva.py, který vypočítá, kolik zaplatíš. V programu
#použij proměnné puvodni_cena, sleva, cena_po_sleve a pomocí nich proveď
#výpočty a vypiš:
#Cena alba je 199 korun
#Sleva činí 20 procent
#Zaplatíš 159.2 korun
#Jakou výslednou cenu program vypíše pro album, jehož původní cena byla 399 korun,
#jestliže sleva činí 30 %?

puvodni_cena=399
sleva=30
zlevnena_cena=puvodni_cena-((puvodni_cena*sleva)/100)
print(zlevnena_cena)