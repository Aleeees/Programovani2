#Mobilní operátor Vegafon počítá platby za přenesená data podle následujících pravidel:
# když za den přeneseš méně než 10 megabajtů dat, zaplatíš za každý megabajt
#2 koruny,
# jinak zaplatíš za celý den 20 korun.
#Napiš program mobilni_data.py, ve kterém do proměnné megabajty přiřadíš počet
#přenesených megabajtů dat za jeden den. Použij příkaz větvení na to, abys do proměnné
#cena přiřadil vyúčtovanou cenu. Nakonec tuto cenu vypiš. Výpis může vypadat například
#takto:
#Zaplatíš 12 korun.
#pro megabajty = 6
#Zaplatíš 20 korun.
#pro megabajty = 20

data=input("Kolik jsi přenesl dat: ")
data= int(data)
if data<10:
    print(f"Zaptatíš {data*2} korun za {data}")
else:
    print(f"Zaplatíš 20korun za {data}")