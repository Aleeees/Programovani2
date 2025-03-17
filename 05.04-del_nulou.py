#Víte, co se stane, když má počítač dělit nulou? Vyzkoušejte to v příkazovém řádku. Potom vytvořte program 04-del_nulou.py, který spočítá převrácenou hodnotu čísla (převrácená hodnota čísla x je rovna 1/x ). Do proměnné n přiřaďte číslo. Použijte příkaz větvení (podmíněný příkaz) a test rovnosti, aby:
#v případě, že n = 0, se zobrazila zpráva Nulou dělit neumím,
#jinak se zobrazil výsledek, například pro n = 10 se zobrazilo 1 / 10 = 0.1.
#Úloha byla převzata z  učebnice Základy programování v jazyce Python pro střední školy od A. Blaha, Ľ. Salanciho a V. Šimandla

number=input("Zadej číšlo k dělení a převrácení hodnoty: ")
number=int(number)
if number==0:
    print("Nulou dělit nelze")
else:
    print(f"číslo {number} má převrácenou hodnotu {1/number}")