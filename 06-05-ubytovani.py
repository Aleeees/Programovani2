# Tento program slouží k výpočtu celkové ceny za ubytování v hotelu
# Host se chce ubytovat na jednu nebo více nocí
#  - cena ubytovani:  800 Kč / osoba a den
# Má možnost si volně zvolit, zda chce snídani; zda chce oběd; zda chce večeři
#  - cena snídaně:     90 Kč / osoba a den
#  - cena oběda:      160 Kč / osoba a den
#  - cena večeře:     120 Kč / osoba a den

# 1. Vypočítejte celkovou cenu za ubytování včetně požadované stravy.
#    Tip: Postup výpočtu je obdobný jako u úkolu jizdne.py
# 2. Program důkladně otestujte pro různé kombinace požadavků
#    - nocí: 2; snídaně:  ne; oběd:  ne; večeře:  ne
#    - nocí: 3; snídaně: ano; oběd: ano; večeře: ano
#    - nocí: 4; snídaně: ano; oběd:  ne; večeře:  ne
# 3. Upravte program tak, aby se uživatele zeptal, zda se bude chtít stravovat
#    Pokud zvolí ano, teprve poté se jej program zeptá, zda bude chtít snídaně / obědy / večeře
# 4. Program důkladně otestujte pro různé kombinace požadavků
#    - nocí: 2; strava: ne
#    - nocí: 3; strava: ano; snídaně: ano; oběd: ano; večeře: ano
#    - nocí: 4; strava: ano; snídaně: ano; oběd:  ne; večeře:  ne
#    - nocí: 5; strava: ano; snídaně: ano; oběd:  ne; večeře:  ano

def pobytStrava(dny,strava):
    strava=strava.lower()
    if strava=="ano":
        snidane = input("Přejete si snídaně? (ano/ne): ")
        obed = input("Přejete si obědy? (ano/ne): ")
        vecere = input("Přejete si večeře? (ano/ne): ")
        pobytVHotelu(dny,snidane,obed,vecere)
    else:
        print("Celková cena za ubytování v našem hotelu bude", dny*800, "Kč")


def pobytVHotelu(dny,snidane,obed,vecere):
    #dnyRet = input("Na kolik nocí se budete chtít ubytovat?: ")
    #dny = int(dnyRet)
    #snidane = input("Přejete si snídaně? (ano/ne): ")
    #obed = input("Přejete si obědy? (ano/ne): ")
    #vecere = input("Přejete si večeře? (ano/ne): ")
    snidane=snidane.lower()
    obed=obed.lower()
    vecere=vecere.lower()
    if snidane=="ano":
        cenaSnidane=dny*90
    else:
        cenaSnidane=0
    if obed=="ano":
        cenaObed=dny*160
    else:
        cenaObed=0
    if vecere=="ano":
        cenaVecere=dny*120
    else:
        cenaVecere=0
    cena = dny*800+cenaSnidane+cenaObed+cenaVecere
    print("Celková cena za ubytování v našem hotelu bude", cena, "Kč")



#    - nocí: 2; snídaně:  ne; oběd:  ne; večeře:  ne
#    - nocí: 3; snídaně: ano; oběd: ano; večeře: ano
#    - nocí: 4; snídaně: ano; oběd:  ne; večeře:  ne
pobytVHotelu(2,"ne","ne","ne")
pobytVHotelu(3,"ano","ano","ano")
pobytVHotelu(4,"ano","ne","ne")

print("Toto je aplikace pro výpočet ceny ubytování. Vítejte")
dnyRet = input("Na kolik nocí se budete chtít ubytovat?: ")
dny = int(dnyRet)
strava=input("Budete chtít jídlo? (ano/ne)")
pobytStrava(dny,strava)