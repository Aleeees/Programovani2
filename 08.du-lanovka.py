print("Toto je aplikace pro výpis času odjezdu lanovky. Vítejte")

# vytvorte program, ktery bude schopen vypsat vsechny odjezdy lanovky mezi
# 9. a 15. hodinou. lanovka odjíždí vždy v :15 a :45
# program otestujte
# pote program upravte, aby simuloval odjezdy lanovky kazdych 10 minut
# (tj 9:00, 9:10, 9:20, ...., 14:50, 15:00)
# program opet otestujte
def vypisPoPulHodine():
    for i in range(9,16):
        print(f"Odjezd lanovky je {i}:15 a {i}:45")

def vypispo10minutach():
    for i in range(9,16):
        cas=00
        for j in range(6):
            print(f"Odjezd lanovky je {i}:{cas if cas!=0 else "00" }")
            cas+=10

vypisPoPulHodine()
vypispo10minutach()