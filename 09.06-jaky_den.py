# Tento program slouží ke generování předpovědi počasi

# 1. Vytvořte pole, které bude obsahovat následující texty: slunečný, polojasný, oblačný, zatažený, deštivý
# 2. Získejte náhodný text z pole a vložte jej do hlášky "Dnes bude ... den"
#    Nápověda: I.   Pomocí generátoru náhodných čísel vygenerujte náhodný index z pole
#              II.  Na základě vygenerovaného čísla získejte prvek nacházející se na daném indexu
#              III. Získaný prvek vložte do hlášky
# 3. Program několikrát spusťte, abyste otestovali jeho funkčnost (měli byste časem získat všechny varianty textů)
# 4. Přidejte do pole nový text - mlhavý
# 5. Program opět několikrát spusťte, abyste otestovali jeho funkčnost
#    (měli byste opět postupně získat všechny varianty textů včetně nového textu mlhavý)

# Převzato z: https://imysleni.cz/ucebnice/zaklady-programovani-v-jazyce-python-pro-stredni-skoly
import random

def predpoved():
    pocasi = ["slunečný", "polojasný", "oblačný", "zatažený", "deštivý","mlhavý"]
    rnd=random.randint(0,len(pocasi)-1)
    return pocasi[rnd]





print(f"Dnde bude {predpoved()} den")