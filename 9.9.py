#Máme „lichou“ hrací kostku, která má na stěnách čísla 1, 3, 5, 7, 9, 11. Uprav předchozí
#program, aby simuloval hod takovou kostkou.
import random as rn
def hod_koskou():
    kostka=[1,3,5,7,9,11]
    return rn.choice(kostka)

print(hod_koskou())