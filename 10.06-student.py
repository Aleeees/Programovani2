# Tato aplikace slouží k výpisu informace, jakou fakultu JU student studuje

# Na textové řetězce lze nahlížet jako na pole znaků.
# Pokud máme text "Ahoj.", pak:
# - znak "A je na indexu 0
# - znak "h je na indexu 1
# - znak "o je na indexu 2
# - znak "j je na indexu 3
# - znak ". je na indexu 4
# Toho lze využít ke zjišťování informací ukrytých v různých textech

# 1. Zjistěte název fakulty, kterou student studuje. Název fakulty je
#    v řetězci zakódován jako 1. znak (např. v čísle P12346 je zkratka
#    fakulty P, čili Pedagogicka fakulta).
#    Zkratky fakult jsou uloženy v poli "zkratky", názvy fakult v poli "fakulty".
#    Zkratka konkrétní fakulty je přitom vždy na stejném indexu jako její nazev.
# 2. Aplikaci otestujte pro následující pspbní čísla:
#    - P12345
#    - A13579
#    - S14703
# 3. Upravte kód, aby pro neexistující zkratku fakulty bylo vypsáno "Student na JU nestuduje"
# 4. Aplikaci otestujte pro následující osobní čísla:
#    - Z15935
#    - C16161

print("Toto je aplikace vypisující informace o studentech. Vítejte")

#osCislo = input("Zadejte osobní číslo studenta: ")
# tvar:P12346

zkratky = ["B", "E", "A", "P", "V", "T", "Z", "S" ]
fakulty=  ["Přírodovědecká fakulta", "Ekonomická fakulta", "Filozofická fakulta", "Pedagogická fakulta", "Fakulta rybářství a ochrany vod", "Teologická fakulta", "Zemědělská fakulta", "Zdravotně sociální fakulta" ]

def informace(os_cislo):
    prvni_znak=os_cislo[0]
    if prvni_znak in zkratky:
        index=zkratky.index(prvni_znak)
        return fakulty[index]
    else:
         return "Student nestuduje na JU."

print(informace('P12345'))
print(informace('A13579'))
print(informace('S14703'))
print(informace('Z15935'))
print(informace('C16161'))