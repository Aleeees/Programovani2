# Tato aplikace slouží k výpisu všech dnů v měsíci

# 1. Vytvořte pole pocetDnu, které bude uchovávat počty dnů v jednotlivých měsících roku
# 2. Doplňte kód, který zajistí uložení správného počtu dnů pro zadaný měsíc do vhodné proměnné
#    Nápověda: Nepoužívejte rozvětvený podmíněný příkaz if-elif-...-elif-else, ale využijte pole z bodu 1)
# 3. Pomocí cyklu a proměnné z bodu 2) vypište datumy všech dnů v zadaném měsíci, např:
#    1 . 3 . 2019
#    2 . 3 . 2019
#    3 . 3 . 2019
#    4 . 3 . 2019
#    ...
#    31 . 3 . 2019
# 4. Program řádně otestujte a řešení ukažte učiteli
# 5. Pokud používáte v programu dvě pole, program optimalizujte, aby bylo použito pouze jedno pole
# 6. Program opět otestujte

print("Toto je aplikace vypisující všechny dny v daném měsíci. Vítejte")


#rok = int(input("Zadejte rok výpisu: "))
#mesic = int(input("Zadejte číslicí měsíc výpisu: "))



def vypisMesice(rok, mesic):
    data={1:31,
          2:28,
          3:31,
          4:30,
          5:30,
          6: 30,
          7: 31,
          8: 31,
          9: 30,
          10: 31,
          11: 30,
          12: 31,}
    for i in range(1,data[mesic]+1):
        print(f'{i}. {mesic}. {rok}')


vypisMesice(1931, 12)