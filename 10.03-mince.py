# Zadání viz soubor 03-mince-zadani.doc

from tkinter import *
import random

canvas = Canvas(width=400, height=300)
canvas.pack()

def mince():
    for i in range(10):
        x = random.randint(20, 380)
        y = random.randint(20, 280)
        hodnota = random.randint(1,5)
        canvas.create_oval(x-20, y-20, x+20, y+20, fill="silver")
        canvas.create_text(x, y, text=hodnota, font='arial 20')

def hodnotaMince():
    hodnotyMince=[1,2,5,10,20,50]
    for i in range(10):
        x = random.randint(20, 380)
        y = random.randint(20, 280)
        hodnota = random.choice(hodnotyMince)
        canvas.create_oval(x-20, y-20, x+20, y+20, fill="silver")
        canvas.create_text(x, y, text=hodnota, font='arial 20')

def hodnotaBarvaMince():
    hodnotyMince=[1,2,5,10,20,50]
    barvaMince=['silver','silver','silver','orange','yellow','gold']
    for i in range(10):
        x = random.randint(20, 380)
        y = random.randint(20, 280)
        hodnota = random.randint(1,5)
        canvas.create_oval(x-20, y-20, x+20, y+20, fill=barvaMince[hodnota])
        canvas.create_text(x, y, text=hodnotyMince[hodnota], font='arial 20')


#mince()
#hodnotaMince()
hodnotaBarvaMince()
mainloop()
