def ratkaisu_ajat(LKM):
    ajat = []
    i = 1
    while i <= LKM:
        luku = float(input("Enter the time for performance {}: ".format(i)))
        ajat.append(luku)
        i += 1
    return ajat


def poista_paras_ja_huonoin(lista_aikoja):
    lista_aikoja.sort()
    del lista_aikoja[0]
    del lista_aikoja[3]
    return lista_aikoja


def laske_keskiarvo(kilpailuajat):
    summa = 0.0
    for aika in kilpailuajat:
        summa += aika

    lukumaara = len(kilpailuajat)
    keskiarvo = summa / lukumaara
    return keskiarvo


def main():
    LKM = 5
    kilpailuajat = poista_paras_ja_huonoin(ratkaisu_ajat(LKM))
    keskiarvo = laske_keskiarvo(kilpailuajat)
    print("The official competition score is {:.2f} seconds.".format(keskiarvo))


main()
