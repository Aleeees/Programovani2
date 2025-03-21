#Mobilní operátor Zodrafon počítá platby za přenesená data podle odlišných pravidel:
# když za den přeneseš méně než 10 megabajtů, zaplatíš za každý megabajt 1 korunu,
# jinak zaplatíš 10 korun a k tomu za každý megabajt nad limit 10 megabajtů 3 koruny.
#Napiš program mobilni_data2.py, který počítá a vypisuje cenu podle těchto pravidel,
#a ověř, zda funguje správně. Program by měl například vypsat:
#Zaplatíš 6 korun.
#pro megabajty = 6
#Zaplatíš 40 korun.
#pro megabajty = 20


data=input("Kolik jsi přenesl dat: ")
data= int(data)
if data<10:
    print(f"Zaptatíš {data*1} korun za {data}")
else:
    print(f"Zaplatíš {((data-10)*3)+10} korun za {data}")