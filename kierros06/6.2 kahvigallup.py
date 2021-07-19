def kysele_kuppien_maaraa():
    tulokset = []

    while True:
        rivi = input()
        if rivi == "":
            break
        else:
            tulokset.append(int(rivi))

    return tulokset


def poista_ei_kahvia_juovat(lista_tuloksista):
    poistettuja = 0
    i = 0

    while i < len(lista_tuloksista):
        if lista_tuloksista[i] == 0:
            del lista_tuloksista[i]
            poistettuja += 1
        else:
            i += 1

    print("Removed {} non-coffee-drinkers responses".format(poistettuja))
    return lista_tuloksista


def tulosta_pylvaat(tulokset):
    korkein = max(tulokset)
    pienin = min(tulokset)
    hash = "#"

    print("")
    print("Information related to coffee drinkers:")
    i = 1

    for i in range(pienin, korkein + 1):
        print("{:2d} {}".format(i, hash * tulokset.count(i)))
        i += 1


def korkein_juoja(tulokset):
    print("")
    print("The greatest response: {} cups of coffee per day".format(
        max(tulokset)))


def yleisin_vastaus(tulokset):
    korkein = max(tulokset)
    pienin = min(tulokset)
    i = 1
    suurin_maara = 0

    for i in range(pienin, korkein + 1):
        if tulokset.count(i) > suurin_maara:
            suurin_maara = tulokset.count(i)

    print("The most common response: {} cups of coffee per day".format(suurin_maara))


def main():

    print("Enter one response per line. End by entering an empty row.")
    tulokset = kysele_kuppien_maaraa()
    poista_ei_kahvia_juovat(tulokset)
    tulosta_pylvaat(tulokset)

    korkein_juoja(tulokset)
    yleisin_vastaus(tulokset)

main()
