# Tento program slouží k výpisu prvních několika přirozených čísel a jejich druhých mocnin

# 1. Vypište pomocí cyklu prvních n přirozených čísel a jejich druhých mocnin.
#    První vypisované číslo nechť je 0, počet vypisovaných čísel závisí na požadavku uživatele
# 2. Program otestujte
# 3. Program upravte tak, aby první vypisované číslo bylo 1
# 4. Program opět otestujte

def vypisCisel():
    print("Toto je aplikace na výpis druhých mocnin přirozených čísel. Vítejte")

    pocet = int(input("Zadejte počet vypisovaných čísel"))
    for i in range(0,pocet):
        print(i*i)

def vypisCiselOd1():
    print("Toto je aplikace na výpis druhých mocnin přirozených čísel. Vítejte")

    pocet = int(input("Zadejte počet vypisovaných čísel"))
    for i in range(1, pocet+1):
        print(i*i)

vypisCisel()
vypisCiselOd1()
