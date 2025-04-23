# Tato aplikace slouží k určení šance, že na 3 hracích kostkách padne určitý součet čísel

# Vytvořte program, který určí, kolikrát na třech klasických kostkách pro "Člověče, nezlob se!"
# padne hodnota 3, hodnota 4, .... hodnota 18

# 1. Vytvořte si pole čísel vhodné velikosti, do nějž budete ukládat, kolikrát která hodnota padla
#    Nápověda: Bez ohledu na počet hodů bude velikost pole menší než 20
# 2. Pro simulaci náhodného hodu použijte funkci randint; součet vytvoříte jako součet tří náhodných hodů (viz kód níže)
# 3. Pomocí cyklu zajistěte počet hodů podle zadání uživatele.
#    Po každém hodu do pole zaznamenejte, že padla daná hodnota - pokud nevíte jak, zejtejte se učitele
# 4. Po skončení "hlavního házejícího cyklu" vypište, kolikrát jaká hodnota padla (např: hodnota 3 padla 100krát)
# 5. Program otestujte - zvolte vysoký počet hodů např. 100 000 popř. 1 000 000
# 6. Výpis z bodu 4 upravte tak, aby vypisoval údaj, v kolika procentech ze všech pokusů padla daná hodnota
# 7. Program opět otestujte - opět zvolte vysoký počet hodů



import random

print("Toto je aplikace pro výpočet pravděpodobnosti výsledku opakovaných hodů kostkou. Vítejte")
n = int(input("Zadejte počet hodů: "))

#soucet = random.randint(1,6) + random.randint(1,6) + random.randint(1,6)
def pravdepodobnost(n):
    hozeno=[0]*16
    for i in range(0,n):
        soucet = random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)
        print(soucet)
        hozeno[soucet-3]+=i
    for i in range(len(hozeno)):
        print(f'{i+3} bylo hozeno {hozeno[i]/n}%, což je {hozeno[i]} z hodů {n}')


pravdepodobnost(n)