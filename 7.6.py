#Teď budeš kreslit čtverec, jehož střed má souřadnice [x, y] a jehož strany mají délku
#100. Souřadnice x, y jsou uloženy ve stejnojmenných proměnných. Abys mohl tento
#čtverec nakreslit, musíš vypočítat souřadnice jeho levého horního i pravého dolního rohu:
#Do nového programu stred_ctverce.py napiš kód, který nakreslí zelený čtverec se
#středem [x, y] a stranou o délce 100.

from tkinter import *

x=200
y=200

create=Canvas()
create.pack()
create.create_rectangle(x-50,y-50,x+50,y+50,fill='green')
mainloop()
