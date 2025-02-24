#Vytvoř nový program pozice_promenne.py a opiš do něj kód uvedený níže.
#V proměnných x, y jsou uložené souřadnice levého horního rohu čtverce. Dokonči kód
#programu tak, abys pomocí uvedených proměnných nakreslil čtverec se stranou délky 100:
from tkinter import *
create = Canvas(width=1000, height=1000)
create.pack()
x = 100
y = 100
create.create_rectangle(x, y, x +100 ,y+100 , fill='yellow')
mainloop()