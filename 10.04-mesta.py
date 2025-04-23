def staty(stat):

    zeme = ["Argentina", "Bolívie", "Brazílie", "Ekvádor", "Guyana", "Chile", "Kolumbie", "Paraguay", "Peru", "Surinam",
            "Trinidad a Tobago", "Uruguay", "Venezuela"]

    mesta = ["Buenos Aires", "La Paz", "Brasília", "Quito", "Georgetown", "Santiago de Chile", "Bogota", "Asunción",
             "Lima", "Paramaribo", "Port of Spain", "Montevideo", "Caracas"]

    mesto = ""
    for i in range(0, len(zeme)):
        if (zeme[i] == stat):
            mesto = mesta[i]

    if (mesto == ""):
        print("Nenalezeno")
    else:
        print(mesto)


staty('Argentina') #Buenos Aires
staty('Peru') #Lima
staty('Venezuela') #Caracas
staty('Mexiko') #Nenalezeno