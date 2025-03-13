#Vytvoř nový program datumy.py – generátor náhodných datumů (pro jednoduchost
#nechť má každý měsíc 30 dní). Po spuštění program vypíše informaci s vygenerovaným
#náhodným datem, například:
#Pokoj si uklidím 30 . 2 . 2025
import random as rn
def datum_uklidu():
    return rn.randint(1,30)

print(f"Pokoj si uklidim dne {datum_uklidu()}.3.2025")
