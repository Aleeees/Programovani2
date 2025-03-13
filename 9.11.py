#Napiš program predpoved.py a v něm podprogram predpoved, který vypíše zprávu
#s předpovědí počasí na dnešní den. Zpráva může vypadat například takto:
#Dnes bude 15 stupňů.
#Jako číselný údaj program zvolí náhodné celé číslo od -15 do 35.
import random as rn

teplota=rn.randint(-15,35)
print(f"Dnes bude {teplota}")