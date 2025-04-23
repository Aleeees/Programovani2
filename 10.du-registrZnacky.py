# Tato aplikace slouží k výpisu informace, z jakého kraje pochází vozidlo dle registrační značky

# 1. Zjistěte kraj, z něhož pochází vozidlo podle zadané registrační značky. Název kraje je
#    v řetězci zakódován jako 2. znak (např. v RZ 5C47891 je zkratka kraje C, čili Jihočeský kraj).
#    Zkratky krajů jsou uloženy v poli "seznamRz", názvy krajů v poli "kraje".
#    Zkratka konkrétního kraje je přitom vždy na stejném indexu jako jeho název.
# 2. Aplikaci otestujte pro následující registrační značky:
#    - 4C20123
#    - 7AM9784
#    - 8S51478
# 3. Upravte kód, aby pro neexistující zkratku kraje bylo vypsáno "Značka na přání, kraj nelze zjistit"
# 4. Aplikaci otestujte pro následující registrační značky:
#    - 4C67215
#    - MOTORKA

print("Toto je aplikace vypisující informace o vozidlech. Vítejte")

rz = input("Zadejte registrační značku vozidla: ")
# tvar: 9C21456

kraje = ['Praha', 'Jihomoravský kraj', 'Jihočeský kraj', 'Pardubický kraj', 'Královéhradecký kraj', 'Kraj Vysočina', 'Karlovarský kraj', 'Liberecký kraj', 'Olomoucký kraj', 'Plzeňský kraj', 'Středočeský kraj', 'Moravskoslezský kraj', 'Ústecký kraj', 'Zlínský kraj']

seznamRz = ['A', 'B', 'C', 'E', 'H', 'J', 'K', 'L', 'M', 'P', 'S', 'T', 'U', 'Z']

def informace(rz):
    znak=rz[1]
    if znak in seznamRz:
        index=seznamRz.index(znak)
        return kraje[index]
    else:
         return "Značka na přání."


print(informace(rz))