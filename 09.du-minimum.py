# Tato aplikace slouží ke zjištění nejmenšího prvku v poli

# 1. Za použití cyklu zjistěte nejmenší prvek v poli pole
#    Použití metody min je zakázáno!
# 2. Nejmenší prvek v poli vypište



print("Toto je aplikace zjišťující minimální prvek v poli. Vítejte")


pole = [80, -54, -16, 54, -93, -53, 69, -87, -95, 80, 37, 24, -79, 68, -69, 10, 99, 7, -4, -68]
nejvetsi=pole[0]
for i in range(len(pole)):
    if nejvetsi>pole[i]:
        nejvetsi=pole[i]
print(nejvetsi)