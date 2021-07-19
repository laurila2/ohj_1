def kysy_lampotilat():
    LKM = 3
    lampotilat = [0.0] * LKM
    i = 0
    print("Anna", LKM, "lampotilaa")
    while i < LKM:
        lampo = float(input("Seuraava lampotila: "))
        lampotilat[i] = lampo
        i += 1
    return lampotilat

def tulosta_lampotilat(lammot):
    print("Annetut lampotilat")
    for arvo in lammot:
        print(arvo)

def laske_keskiarvo(lampotilalista):
    summa = 0.0
    for lampotila in lampotilalista:
        summa += lampotila
    lukumaara = len(lampotilalista)
    if lukumaara > 0:
        keskiarvo = summa / lukumaara
    else:
        keskiarvo = 0.0
    return keskiarvo

def main():
    lampolista = kysy_lampotilat()
    tulosta_lampotilat(lampolista)
    keskiarvo = laske_keskiarvo(lampolista)
    print("Lampotilojen keskiarvo on {:.2f}".format(keskiarvo))

main()