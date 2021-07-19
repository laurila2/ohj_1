def main():

    nimi = str(input("Enter the name of the file: "))
    #nimi = "file7.txt"

    try:
        lahdetiedosto = open(nimi, "r")
        rivilista = lahdetiedosto.readlines()
        lahdetiedosto.close()
    except OSError:
        print("Error: file {} cannot be read.".format(nimi))
        return

    maksut = {}

    try:
        for rivi in rivilista:
            rivi = rivi.rstrip()
            tiedot = rivi.split(":")
            nimi = tiedot[0]
            maksu = float(tiedot[1])

            if nimi not in maksut:
                maksut[nimi] = [maksu]
            else:
                maksut[nimi].append(maksu)
    except (ValueError, IndexError):
        print("Error: there was an erroneous line in the file.")
        return

    total = 0

    for nimi in maksut:
        total += sum(maksut[nimi])
    print("Total costs: {0:.2f}e".format(total))
    print("")

    individual_payment = total / (len(maksut))

    for nimi in sorted(maksut):

        maksut_merkkijono = ""
        for i in range(len(maksut[nimi])):
            luku = "{:.2f}".format(maksut[nimi][i])
            luku = str(luku)

            if i < (len(maksut[nimi]) - 1):
                maksut_merkkijono += luku + ", "
            else:
                maksut_merkkijono += luku

        erotus = float(sum(maksut[nimi]) - individual_payment)

        if abs(erotus) < 0.05:
            print("{} has paid {:.2f} in the following amounts: {}".format(nimi, sum(maksut[nimi]), maksut_merkkijono))
            print("No transfers needed.")
            print("")
        elif erotus > 0:
            print("{} has paid {:.2f} in the following amounts: {}".format(nimi, sum(maksut[nimi]),
                                                                           maksut_merkkijono))
            print(nimi, "needs to receive %.2fe." % erotus)
            print("")
        elif erotus < 0:
            print("{} has paid {:.2f} in the following amounts: {}".format(nimi, sum(maksut[nimi]),
                                                                           maksut_merkkijono))
            print(nimi, "needs to pay %.2fe." % abs(erotus))
            print("")


main()
