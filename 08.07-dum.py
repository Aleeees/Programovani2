# Tento program slouží k nakreslení několikapatrového domu

# 1. Pomocí for cyklu zajistěte nakreslení oken v jednom patře domu (cca 6 oken)
# 2. Program otestujte
# 3. Zajistěte, aby se nakreslilo několik pater domu (cca 8 pater)
#   Pozor, kód programu se nesmí opakovat!
# 4. Program otestujte

from tkinter import *

canvas = Canvas(width=500, height=800)
canvas.pack()


canvas.create_rectangle(20, 150, 480, 750, fill="blanchedalmond")
canvas.create_polygon(20, 150, 480, 150, 400, 50, 100, 50, fill="red")
x = 50
for i in range(6):
    y = 180
    for j in range(8):
        canvas.create_rectangle(x, y, x + 50, y + 50, fill="blue")
        y+=70
    x+=70
mainloop()

