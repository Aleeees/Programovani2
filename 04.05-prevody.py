# Tento program slouzi k převodům časových jednotek
# Uživatel zadává vždy počet sekund a program na jeho základě vypíše,
# kolik je to celých minut a kolik sekund
# Příklad: Uživatel zadá 144 sekund -> program vypíše 2 min 24 sekund
# Poté program na další řádek vypíše, kolik je to minut (v desetinném tvaru)
# Příklad: Pro 144 sekund program vypíše 2.4 minut
from Cviceni1 import sekund

# 1. Promyslete, jak výpočet převodu probíhá bez použití počítače
# 2. Doplňte na vhodné místo v kódu potřebný výpočet pro výpis ve tvaru minuty - sekundy
# 3. Program otestujte 
# 4. Doplňte na vhodné místo v kódu potřebný výpočet pro výpis v minutách
# 5. Program opět otestujte 

print("Toto je aplikace pro výpis času v různých formátech. Vítejte")

sekRet = input("Zadejte počet sekund: ")
sek = int(sekRet)



# zde doplnte potrebny kod
min=sek/60
print(f"{sek} je {min} minuty.")


