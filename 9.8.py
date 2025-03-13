#Máme „sudou“ hrací kostku, která má na stěnách čísla 2, 4, 6, 8, 10, 12. Uprav předchozí
#program, aby simuloval hod takovou kostkou.
import random as rn
def hod_koskou():
    kostka=[2,4,6,8,10,12]
    return rn.choice(kostka)

print(hod_koskou())
