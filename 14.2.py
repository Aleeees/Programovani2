#V jazyce Python kreslíme elipsy a kruhy příkazem create_oval. Vytvoř nový program
#elipsa.py a zapiš do něj následující kód:
import tkinter
from tkinter import mainloop

canvas = tkinter.Canvas()
canvas.pack()
canvas.create_oval(10, 10, 200, 150)
mainloop()
#Vyzkoušej, co program nakreslí.