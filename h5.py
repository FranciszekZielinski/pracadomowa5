def sprawdz_klucz(klucz):
    if klucz == "":
        return False

    if len(klucz) % 2 != 0:
        print("Błąd! Znak bez pary")
        return False

    if len(set(klucz)) != len(klucz):
        print("Błąd! Szyfr nie jest jednoznaczny")
        return False

    return True


def zrob_klucz(klucz):
    szyfr = {}
    i = 0
    j = 1

    while j < len(klucz):
        szyfr[klucz[i].lower()] = klucz[j].lower()
        szyfr[klucz[j].lower()] = klucz[i].lower()
        i = j + 1
        j = i + 1

    return szyfr


def zakoduj(kod, tresc):
    tekst = ""
    for x in tresc:
        if x.lower() in kod.keys():
            if x.isupper():
                tekst += kod[x.lower()].upper()
            else:
                tekst += kod[x.lower()]
        else:
            tekst += x
    return tekst


def zakoduj2(wiadomosc, klucz):
    if klucz == "gaderypoluki" or klucz == "GADERYPOLUKI":
        s = zrob_klucz("gaderypoluki")
        return zakoduj(s, wiadomosc)
    elif klucz == "politykarenu" or klucz == "POLITYKARENU":
        s = zrob_klucz("politykarenu")
        return zakoduj(s, wiadomosc)
    else:
        if sprawdz_klucz(klucz):
            s = zrob_klucz(klucz)
            return zakoduj(s, wiadomosc)


def odkoduj(kod, tresc):
    return zakoduj2(kod, tresc)


co_chcesz = input("chcesz odszyfrować czy zaszyfrować? o/z ")
wiadomosc = input("podaj wiadomosc ")
szyfr = input("podaj szyfr podstawieniowy: gaderypoluki/politykarenu/lub swój własny ")

if co_chcesz == "o":
    print(odkoduj(wiadomosc, szyfr))
elif co_chcesz == "z":
    print(zakoduj2(wiadomosc, szyfr))
