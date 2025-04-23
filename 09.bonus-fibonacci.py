# Tato aplikace slouží k výpisu prvních několika prvků Fibonacciho posloupnosti
# Fibonacciho posloupnost je řada čísel, kde:
# - 1. číslo je 0
# - 2. číslo je 1
# - každé další číslo je součtem předchozích dvou čísel
# tj. začátek řady je 0, 1, 1, 2, 3, 5, 8, 13, 21, ...

# 1. Vytvořte pole o velikosti n
# 2. Na první dvě pozice v poli uložte čísla 0 a 1
# 3. Vytvořte kód, který zajistí naplnění zbytku pole správnými hodnotami
# 4. Zajistěte výpis celého pole
# 5. Aplikace řádně otestujte pro následující n:
#    - n = 5
#    - n = 10
#    - n = 31
#    - n = 3
#    - n = 2
#    - n = 1


print("Toto je aplikace vypisující Fibonacciho posloupnost. Vítejte")

vstup = input("Zadejte počet hledaných prvků: ")
pocetPrvku=int(vstup)


def fibonacci(pocet_prvku):
    posloupnost = [0, 1]
    if pocet_prvku == 1:
        return [0]

    for i in range(2, pocet_prvku):
        posloupnost.append(posloupnost[i - 1] + posloupnost[i - 2])

    return posloupnost[:pocet_prvku]

print(fibonacci(pocetPrvku))