from random import randint as rnd



def dveKostky():
    for i in range(5):
        prvni=rnd(1,6)
        druha=rnd(1,6)
        print(f"Na první kostce padlo číslo {prvni}\n"
              f"Na druhé kostce padlo číslo {druha}\n"
              f"Součet čísel je {prvni+druha}\n")


dveKostky()