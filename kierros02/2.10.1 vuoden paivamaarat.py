

# Ohjelma tulostaa vuoden 2014 jokaisen perjantain päivämäärän.
# Ensimmäinen perjantai oli 3.1.


def main():
    laskuri = 4
    for kuukaudet in range(1, 13):
        if kuukaudet == 2:
            for paivat in range(1, 29):
                laskuri = laskuri + 1
                if (laskuri % 7) == 0:
                    print(paivat, ".", kuukaudet, ".", sep="")
        elif kuukaudet == 1 or kuukaudet == 3 or kuukaudet == 5 or kuukaudet == 7 or kuukaudet == 8 or kuukaudet == 10 or kuukaudet == 12:
            for paivat in range(1, 32):
                laskuri = laskuri + 1
                if (laskuri % 7) == 0:
                    print(paivat, ".", kuukaudet, ".", sep="")
        else:
            for paivat in range(1, 31):
                laskuri = laskuri + 1
                if (laskuri % 7) == 0:
                    print(paivat, ".", kuukaudet, ".", sep="")
    #print(laskuri)


main()
