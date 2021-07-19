def read_inputfile(filename):
    kaupat = {}
    tuotteet = {}

    try:
        tiedosto = open(filename, "r")
        rivilista = tiedosto.readlines()
        tiedosto.close()

        for rivi in rivilista:
            rivi = rivi.rstrip()
            tiedot = rivi.split(":")

            kauppa = tiedot[0]
            tuote = tiedot[1]
            hinta = tiedot[2]

            if kauppa not in kaupat:
                kaupat[kauppa] = {}

            kaupat[kauppa][tuote] = hinta

            # sanakirja tuoteet ja sen halvin hinta
            if tuote not in tuotteet:
                tuotteet[tuote] = hinta
            elif hinta < tuotteet[tuote]:
                tuotteet[tuote] = hinta
        print(kaupat)
        print(tuotteet)

    except OSError:
        print(f"Error: file {filename} cannot be read.")

    return kaupat, tuotteet

read_inputfile("products.txt")
