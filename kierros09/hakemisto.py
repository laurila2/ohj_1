# TIE-02100 Johdatus ohjelmointiin
# Esimerkkiohjelma, kirjan aakkosellisen hakemiston muodostaminen

def main():
    hakemisto = {}
    syotetiedoston_nimi = input("Syötetiedosto: ")
    try:
        tiedosto_olio = open(syotetiedoston_nimi, "r")
        for rivi in tiedosto_olio:
            tiedot = rivi.split()
            if len(tiedot) != 2:
                raise ValueError("Virheellinen rivi, sivunumero puuttuu")

            hakusana = tiedot[0]
            sivunumero = int(tiedot[1])

            if sivunumero < 0:
                raise ValueError("Virheellinen sivunumero")

            if hakusana not in hakemisto:
                hakemisto[hakusana] = [sivunumero]
            else:
                hakemisto[hakusana].append(sivunumero)

    except OSError:
        print("Tiedoston lukemisessa tapahtui virhe!")

    except ValueError as virheilmoitus:
        print("Virhe:", virheilmoitus)

    tulostetiedoston_nimi = input("Tulostetiedosto: ")
    try:
        tiedosto_olio = open(tulostetiedoston_nimi, "w")
        for sana in sorted(hakemisto):
            print(sana, "", end="", file=tiedosto_olio)
            for sivu in sorted(hakemisto[sana]):
                print(sivu, "", end="", file=tiedosto_olio)
            print(file=tiedosto_olio)
    except OSError:
        print("Tiedostoon kirjoittamisessa tapahtui virhe!")


main()
