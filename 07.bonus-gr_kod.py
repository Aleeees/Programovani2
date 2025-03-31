from tkinter import *
import random as rnd



def qr_kod():
    create=Canvas(width=210, height=210)
    create.pack()
    for row in range(21):
        for col in range(21):
            if rnd.randint(0, 1) == 1:
                x = col * 10
                y = row * 10
                create.create_rectangle(x, y, x + 10, y + 10, fill="black", outline="black")


qr_kod()
mainloop()