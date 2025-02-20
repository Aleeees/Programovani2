from tkinter import *
#Přidej do programu vybarveny.py další 3 příkazy na kreslení obdélníků, abys dostal následující obrázek:
create = Canvas(width=1000, height=1000)
create.pack()
create.create_rectangle(50, 50, 100, 100,fill="red")
create.create_rectangle(110, 50, 160, 100,fill="green")
create.create_rectangle(50, 110, 100, 160,fill="blue")
create.create_rectangle(110, 110, 160, 160,fill="yellow")

#Vytvoř nový program nizozemi.py, který nakreslí nizozemskou vlajku:
create.create_rectangle(200, 100, 350, 130,fill="red")
create.create_rectangle(200, 130, 350, 160,fill="white")
create.create_rectangle(200, 160, 350, 190,fill="blue")

#Vytvoř nový program irsko.py, který nakreslí irskou vlajku:
create.create_rectangle(400, 100, 430, 150,fill="green")
create.create_rectangle(430, 100, 460, 150,fill="white")
create.create_rectangle(460, 100, 490, 150,fill="orange")


#Vytvoř nový program irsko.py, který nakreslí irskou vlajku:
create.create_rectangle(500, 100, 900, 300,fill="white")
create.create_rectangle(550, 100, 600, 300,fill="blue")
create.create_rectangle(500, 175, 900, 225,fill="blue")

#Vytvoř nový program norsko.py, který nakreslí norskou vlajku:
create.create_rectangle(500, 100, 900, 300,fill="white")
create.create_rectangle(550, 100, 600, 300,fill="blue")
create.create_rectangle(500, 175, 900, 225,fill="blue")
mainloop()