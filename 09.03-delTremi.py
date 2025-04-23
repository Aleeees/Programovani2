# Tato aplikace slouží ke zjištění, kolik čísel v poli je dělitelných třemi

# 1. Vytvořte kód, který vypíše všechny prvky v poli, které jsou dělitelné třemi beze zbytku
#    (tj. zbytek po dělení třemi je roven nule)
# 2. Kód otestujte
# 3. Upravte předchozí kód tak, aby na konec výpisu vypsal počet, kolik prvků v poli je dělitelných třemi beze zbytku
# 4. Kód otestujte

print("Toto je aplikace zjišťující počet prvků dělitelných třemi. Vítejte")


pole = [80, 54, 16, 54, 99, 53, 69, 87, 93, 80, 37, 24, 79, 68, 69, 10, 99, 19, 22, 68]
delitelne=0
for i in range(len(pole)):
    if pole[i]%3==0:
        print(pole[i])
        delitelne+=1
print(f"Počet dělitelných 3 je {delitelne}")
