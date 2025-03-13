#Máme exotickou hrací kostku, která má na stěnách čísla 1, 4, 9, 16, 25, 36. Uprav
#předchozí program, aby simuloval hod takovou kostkou
import random as rn
def hod_koskou():
    kostka=[1,4,9,16,25,36]
    return rn.choice(kostka)

print(hod_koskou())