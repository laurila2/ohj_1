def main():
    print("Ohjelma kirjoittaa vieraslistan haluamaasi tiedostoon.")
    nimi = input("Anna kirjoitettavan tiedoston nimi: ")
    try:
        tulostiedosto = open(nimi, "w")
        print("Anna tallennettavat nimet.")
        print("Lopeta tyhjalla rivilla.")
        rivi = input()
        while rivi != "":
            print(rivi, file=tulostiedosto)
            rivi = input()
        tulostiedosto.close()
        print("Nimet on kirjoitettu tiedostoon", nimi)
    except OSError:
        print("Virhe tiedoston", nimi, "kirjoittamisessa. Ohjelma paattyy.")


main()