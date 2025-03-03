#Diskutuj se sousedem, jak nakreslit kruh. Potom změň předchozí program tak, aby se místo
#věže kreslil sněhulák.
from tkinter import *
canvas= Canvas()
canvas.pack()
canvas.create_oval(170,50,210,90)
canvas.create_oval(160,90,220,150)
canvas.create_oval(150,150,230,230)



mainloop()