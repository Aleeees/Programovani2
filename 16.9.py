#Jdeme na zmrzlinu. Cena za jeden kopeček zmrzliny je 25 korun. Zmrzlinář však nabízí
#slevu: když vezmeme víc než 4 kopečky, cena za každý kopeček bude 20 korun. Vytvoř
#program zmrzlina.py, ve kterém na začátku přiřadíš do proměnné pocet počet
#kopečků a on vypíše výslednou cenu. Například:
#Za 5 kopečků zmrzliny zaplatíš:
#100 korun.
#Ověř, že program správně počítá cenu zmrzliny pro 4, 5 a 6 kopečků

kopecky= input("Kolik chceš kopečku: ")
kopecky = int(kopecky)
if kopecky>4:
    cenu=kopecky*20
else:
    cenu=kopecky*25

print(f"Zaplať {cenu}Kč")