#Chceš porovnat svůj věk s věkem kamarádky. Vytvoř program porovnani_veku.py, ve
#kterém do proměnných ja a ona přiřadíš svůj věk a věk tvé kamarádky. Program tyto
#údaje porovná a podle toho vypíše: Jsme stejně staří, Jsem mladší nebo Ona
#je mladší.
def porovnaniVeku(muj,jeji):
    if muj == jeji:
        print("Jsme stejně staří")
    elif muj > jeji:
        print("Jsem starší")
    elif muj < jeji:
        print("Jsi starší")


porovnaniVeku(19,20)
porovnaniVeku(21,20)
porovnaniVeku(20,20)