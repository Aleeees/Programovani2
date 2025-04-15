# Tato aplikace slouží ke zjištění, jaká čísla v poli jsou větší než 50

# 1. Vytvořte kód, který vypíše všechny prvky v poli, které jsou větší než 50
# 2. Kód otestujte


print("Toto je aplikace zjišťující prvky, které jsou větší než 50. Vítejte")


pole = [80, 54, 16, 54, 99, 53, 69, 87, 93, 80, 37, 24, 79, 68, 69, 10, 99, 19, 22, 68]
for i in range(len(pole)):
    if pole[i]>50:
        print(pole[i])
