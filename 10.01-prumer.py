# Tato aplikace slouží k výpočtu průměrného počtu bodů studentů v testu a k výpisu počtu bodů každého studenta

# 1. Vytvořte kód, pomocí kterého vypíšete průměrný počet bodů dosažených studenty v testu
# 2. Program otestujte
# 3. Vymažte z obou polí první prvek (tj. hodnoty 80 a "Adam")
# 4. Program znovu otestujte a řešení ukažte učiteli
# 5. Vytvořte kód, který vypíše dvojice hodnot student - počet bodů.
#    Předpokládejte, že obě pole mají stejný počet prvků a že si odpovídají hodnoty na stejných indexech
#    tj. vznikají dvojice "Barbora: 54 bodů", "Cyril: 16 bodů" apod.
# 6. Program otestujte a řešení ukažte učiteli


print("Toto je aplikace zjišťující výsledky testu. Vítejte")


znamky = [80, 54, 16, 54, 99, 53, 69, 87, 93, 80, 37, 24, 79, 68, 69, 10, 99, 19, 22, 68]
studenti = ["Adam", "Barbora", "Cyril", "David", "Daniel", "Dana", "Eva", "Evžen",
            "František", "Gábina", "Hana", "Hynek", "Karel", "Klára", "Ludmila", "Luděk",
            "Martina", "Markéta", "Milan", "Mirek"]


def prumer(znamky):
    vysledek=0
    for i in range(len(znamky)):
        vysledek+= znamky[i]
    vysledek /= len(znamky)
    return vysledek



def dvojice(studenti,znamky):
    for i in range(len(znamky)):
        print(f'{studenti[i]} má {znamky[i]} bodů')

print(f'Prumer bodu ve třídě je {prumer(znamky)}')
dvojice(studenti,znamky)