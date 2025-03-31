# 1. Pomoci for cyklu vytvořte program, který pod sebe vypíše následujících 10 řádků textu:
#  číslo 0
#  číslo 1
#  číslo 2
#  číslo 3
#  číslo 4
#  číslo 5
#  číslo 6
#  číslo 7
#  číslo 8
#  číslo 9

# 2. Pod výše uvedený kód napište kód pro druhou verzi výpisu - ten výpíše pod sebe čísla
#  0, 1, 2, ... 10 – tedy i číslo 10

# 3. Pod výše uvedený kód napište kód pro třetí verzi výpisu - ten výpíše pod sebe čísla
#  1, 2, 3, ... 10

# 4. Pod výše uvedený kód napište kód pro čtvrtou verzi výpisu - ten výpíše pod sebe čísla
#  2, 4, 6, ... 20

# 5. Pod výše uvedený kód napište kód pro pátou verzi výpisu - ten výpíše pod sebe čísla
#  1, 3, 5, ... 19


# Převzato z: https://imysleni.cz/ucebnice/zaklady-programovani-v-jazyce-python-pro-stredni-skoly
def prvniVerze():
    for i in range(0,10):
        print(f"číslo {i}")

def druhaVerze():
    for i in range(1,11):
        print(f"číslo {i}")

def tretiVerze():
    for i in range(1,11,2):
        print(f"číslo {i}")

def ctvrtaVerze():
    for i in range(0,22,2):
        print(f"číslo {i}")

def pataVerze():
    for i in range(1,20,2):
        print(f"číslo {i}")




prvniVerze()
druhaVerze()
tretiVerze()
ctvrtaVerze()
pataVerze()