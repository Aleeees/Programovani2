import tkinter
from datetime import datetime
from tkinter import *



vek= 16
dni=(vek*12+2)*30
print(str(dni) + " dni stary")
hodin=dni*24
print(str(hodin) + " hodin")
sekund=hodin*60
print(str(sekund) + " sekund")


#Použij znovu Python jako kalkulačku a vytvoř pro něj zápis, pomocí kterého vypočítá
#součet všech lichých čísel od 1 do 19. Jaký bude výsledek?
liche=0
for i in range(1,19):
    if i%2==0:
        liche+=i
        print(liche)


#Použij Python jako kalkulačku a vypočítej součet následujících čísel: jedna, jedna polovina, jedna třetina, jedna čtvrtina, …, až jedna desetina.
soucet=0
for i in range(1,10):
    vydel=1/i
    soucet+=vydel
    print(soucet)


#Přepni se zpět do svého programu a přidej další příkaz print, kterým vypíšeš text„Dnes je středa“ (místo středy doplň aktuální den v týdnu). Program ulož a spusť jej.
print(datetime.today().strftime("%A"))




#Vytvoř program basnicka.py, který vypíše úryvek tvé oblíbené básničky nebo písničky. Jestli tě žádná nenapadá, můžeš vypsat tuto básničku:
print("Na topole nad jezerem \n seděl vodník podvečerem: \n Sviť, měsíčku, sviť, \n ať mi šije niť.")


create = Canvas(width=1000, height=300)
create.pack()
create.create_rectangle(50, 30, 250, 170)
create.create_rectangle(200, 100, 60, 140)
#vedle sebe
create.create_rectangle(400, 100, 460, 60)
create.create_rectangle(480, 100, 540, 60)
#Vytvoř program soustredne.py, který nakreslí dva velké čtverce – jeden se stranou délky 100 a druhý 150. Čtverce budou mít společný střed jako na následujícím obrázku:
create = Canvas(width=1000, height=300)
create.pack()
create.create_rectangle(100, 30, 200, 130)
create.create_rectangle(75, 5, 225, 155)
#Vytvoř program pyramida.py, který ze tří obdélníků o rozměrech 150x50, 100x50 a 50x50 nakreslí následující pyramidu
create = Canvas(width=1000, height=300)
create.pack()
create.create_rectangle(200, 30, 250, 80)
create.create_rectangle(175, 80, 275, 130)
create.create_rectangle(150, 130, 300, 180)

