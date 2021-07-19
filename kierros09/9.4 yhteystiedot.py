


def read_file(file):

    tiedosto = open(file, "r")
    rivilista = tiedosto.readlines()
    tiedosto.close()

    print(rivilista)


    sanakirja = {}

    for rivi in rivilista:
        rivi = rivi.rstrip()
        tiedot = rivi.split(";")

    if avain not in sanakirja:


    print(tiedot)



read_file("contacts.csv")




