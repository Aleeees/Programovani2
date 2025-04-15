# Tento program jen spuťte, kód se zde nedoplňuje

import tkinter
import random
import time

canvas = tkinter.Canvas(width=400, height=300)
canvas.pack()

txt=canvas.create_text(200, 100, text="Nyní promítneme 10 čísel,\n z nichž určete maximum", font='arial 16')
canvas.update()
time.sleep(5)
canvas.delete(txt)

for i in range (0,10):
    txt=canvas.create_text(200, 100, text=random.randint(1,random.randint(1,80)), font='arial 30')
    canvas.update()
    time.sleep(2)
    canvas.delete(txt)


txt=canvas.create_text(200, 150, text="A) Kolik bylo maximum?\nB) Jak jste to zjistili?\n\nPokud A) víte a B) nevíte, \npusťte si program znovu", font='arial 16')
canvas.update()

