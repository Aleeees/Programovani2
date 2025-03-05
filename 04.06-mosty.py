# Toto je aplikace sloužící k výpočtu maximální hmotnosti vozu na cestě z místa A do místa B
# Po cestě jsou tři mosty, z nichž má každý určitou nosnost
# Zjistěte, jak může být vůz maximálně těžký, aby bezpečně projel

# 1. Vypočítejte maximální možnou hmotnost vozu
#    - Tip: Použijte vhodnou funkci
# 2. Program otestuje pro následující hodnoty:
#    - most1: 5, most2: 8, most3: 6
#    - most1: 8, most2: 5, most3: 13 
# 3. Uživatel mohl zadat omylem záporné hodnoty -> zajistěte, aby záporná čísla
#    byla převedena na absolutní hodnoty těchto čísel (nepoužívejte podmíněný přkaz)
# 4. Program otestuje pro následující hodnoty:
#    - most1: 5, most2: 8, most3: -6
#    - most1: 8, most2: 5, most3: -13 

print("Toto je aplikace pro maximální hmotnosti vozu po cestě z místa A do B. Vítejte")

most1 = input("Zadejte nosnost prvního mostu: ")
most2 = input("Zadejte nosnost druhého mostu: ")
most3 = input("Zadejte nosnost třetího mostu: ")

# zde doplňte potřebný kód

vysledek = 0
print("Maximální možná hmotnost vozu je", vysledek)
