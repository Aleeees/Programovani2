# 1. Pomoci for cyklu vytvořte program, který pod sebe pětkrát vypíše následující dva řádky textu:
#  Těším se na prázdniny
#  =====================
#
# 2. Pod výše uvedený kód napište kód pro druhou verzi výpisu - ten výpíše pětkrát pouze
#    text "Těším se na prázdniny", ale řádek "=====================" vypíše jen jednou

# Převzato z: https://imysleni.cz/ucebnice/zaklady-programovani-v-jazyce-python-pro-stredni-skoly


def pozdrav():
    for i in range(1,6):
        print("Těším se na prázdniny")
    print("==========================")



pozdrav()