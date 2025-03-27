#V televizní soutěži o pečení Můj děda peče líp než tvůj jsou následující pravidla:
# když soutěžící stihne upéct méně než 10 koláčků, je hodnocen jako začátečník,
# když stihne upéct aspoň 10, ale méně než 20 koláčků, je hodnocen jako pokročilý,
# když stihne upéct aspoň 20 koláčků, je hodnocen jako expert.
#Vytvoř nový program kolacky.py, ve kterém přiřadíš do proměnné kolace počet
#upečených koláčků. Program poté rozhodne, zda je daný soutěžící začátečník, pokročilý
#nebo expert, a vypíše vhodnou hlášku.
#Otestuj, zda program zobrazí správnou hlášku pro následující počty upečených koláčků: 1,
#9, 10, 19, 20, 100.

def mujDedaPeceLipNezTvuj(upecene):
    if upecene<10:
        print("Jsi začátečník")
    elif upecene < 20:
        print("Pokročilý")
    elif upecene>=20:
        print("Expert")


mujDedaPeceLipNezTvuj(1)
mujDedaPeceLipNezTvuj(9)
mujDedaPeceLipNezTvuj(10)
mujDedaPeceLipNezTvuj(19)
mujDedaPeceLipNezTvuj(20)
mujDedaPeceLipNezTvuj(100)