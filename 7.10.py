#Napiš program mimozemstan.py, který pomocí barevných obdélníků nakreslí hlavu
#mimozemšťana. Na hlavě by měly být minimálně dvě stejné oči a jedna ústa. Souřadnice
#středu hlavy jsou uloženy v proměnných x, y.
#Bude program fungovat správně i v případě, že hodnotu proměnné x zvětšíš o 30
#a hodnotu proměnné y zvětšíš o 40? Jestli ne, program oprav.


from tkinter import *

x=200
y=200

create=Canvas(width=400,height=400)
create.pack()
create.create_oval(x-100,y-100,x+100,y+100,fill="green")
create.create_oval(x-30,y+50,x+30,y+20,fill="red")
create.create_rectangle(x-50,y-30,x-15,y,fill="blue")
create.create_rectangle(x+50,y-30,x+15,y,fill="blue")
create.create_oval(x-30,y-27,x-20,y-18,fill="white")
create.create_oval(x+30,y-27,x+20,y-18,fill="white")

mainloop()