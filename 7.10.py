#Napiš program mimozemstan.py, který pomocí barevných obdélníků nakreslí hlavu
#mimozemšťana. Na hlavě by měly být minimálně dvě stejné oči a jedna ústa. Souřadnice
#středu hlavy jsou uloženy v proměnných x, y.
#Bude program fungovat správně i v případě, že hodnotu proměnné x zvětšíš o 30
#a hodnotu proměnné y zvětšíš o 40? Jestli ne, program oprav.


from tkinter import *

x=100
y=100

create=Canvas()
create.pack()
mainloop()