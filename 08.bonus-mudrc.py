def zrnkaSachovnice():
    zrno=0
    for i in range(1,65):
        zrno+=i*10
    return zrno


def jinaPovest():
    zrno=1
    for i in range(1,65):
        zrno=zrno*2
    return zrno

print(f"Odměna bude {zrnkaSachovnice()} zrn")
print(f"Odměna bude {jinaPovest()} zrn")