# Tento program slouží k výpočtu součinu prvních n přirozených čísel

# 1. Vytvořte kód, který bude počítat součin prvních N přirozených čísel
#    přílad: n=5 -> soucin = 1*2*3*4*5=120
# 2. Program řádně otestujte


print("Toto je aplikace umožňující součin několika prvních přirozených čísel. Vítejte")
n = int(input("Zadejte počet násobených čísel: "))
vysledek=1
for i in range(1,n+1):
    vysledek*=i

print(vysledek)

