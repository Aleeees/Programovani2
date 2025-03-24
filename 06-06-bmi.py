# Tato aplikace slouží k výpočtu BMI a ke slovnímu hodnocení zjištěného BMI

# 1. Vypočítejte BMI a vypište jej (vzorec pro výpočet naleznete na internetu)
# 2. Program otestujte, zda funguje správně (Vaše BMI by mělo být cca mezi 18 a 30)
# 3. Utvořte slovní hodnocení zjištěného BMI:
##     těžká podvýživa:       ≤ 16,5
##     podváha:               16,5–18,5
##     ideální (zdravá) váha: 18,5–25
##     nadváha:               25–30 
##     mírná obezita:         30–35
##     střední obezita:       35–40
##     morbidní obezita:      > 40
# 4. Program důkladně otestujte
# 5. Program optimalizujte, aby v podmínkách nebyly použity operátory AND a OR
# 6. Program opět otestujte


print("Toto je aplikace pro výpočet BMI. Vítejte")
hmotnostRet = input("Zadejte hmotnost v kg: ")
vyskaRet = input("Zadejte vysku v cm: ")
def BMI(hmotnostRet,vyskaRet):
    hmotnost = int(hmotnostRet)
    vyska = int(vyskaRet)
    vyska=vyska/100
    bmi=hmotnost/(vyska*vyska)
    if bmi <= 16.5:
        vysledek="těžká podvýživa"
    elif bmi > 16.5 and bmi < 18.5:
        vysledek="podvaha"
    elif bmi >= 18.5 and bmi < 25:
        vysledek="normalni vaha"
    elif bmi >= 25 and bmi < 30:
        vysledek="nadvaha"
    elif bmi >= 30 and bmi < 35:
        vysledek= "mirna obezita"
    elif bmi >= 35 and bmi < 40:
        vysledek="střední obezita"
    elif bmi >= 40:
        vysledek="morbidní obezita"
    else:
        vysledek="DEATH"
    print(vysledek)


BMI(90,180)