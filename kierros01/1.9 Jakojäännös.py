
def main():
    rivi = input("Anna aikajakson pituus sekunteina.\n")
    pituus_sekunteina = int(rivi)
    tunnit = pituus_sekunteina // 3600
    jaannossekunnit = pituus_sekunteina % 3600
    minuutit = jaannossekunnit // 60
    sekunnit = jaannossekunnit % 60
    print("Pituus on", tunnit, "h", minuutit, "min", sekunnit, "s.")


main()
