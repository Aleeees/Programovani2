#Uprav předchozí program tak, aby se nejdříve do proměnných x, y přiřadily souřadnice
#středu kruhu a ty se potom použily v příkazech create_oval. Kromě toho přidej na
#úplný konec programu i kreslení zeleného obdélníku, který bude představovat krajinu.
#Potom program pro x = 200 a y = 150 bude kreslit scény jako na následujících
#obrázcích:
#pro cas = 4
#pro cas = 14
#Horní okraj zeleného obdélníku umísti na y-ovou souřadnici 180.

from tkinter import *
create= Canvas()
create.pack()

cas= input("Kolik je hodin: ")
cas= int(cas)
x=200
y=100
if cas<8:
    barva="white"
    pozadi="lightblue"
if cas==4:
    x=200
    y=150
if cas==14:
    x=200
    y=150
else:
    barva="yellow"
    pozadi="darkblue"

create.create_rectangle(100,0,300,200,fill=pozadi)
create.create_oval(x-25,y-25,x+25,y+25,fill=barva)
create.create_rectangle(100,150,300,200,fill="green")


mainloop()