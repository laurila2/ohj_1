def laske_arvokehitys(paaoma, aika, tuottoprosentti):
    print("Sijoituksen arvo vuoden lopussa:")
    print("vuosi  arvo")
    for i in range(1, aika + 1):
        paaoma = paaoma * (1.0 + tuottoprosentti / 100.0)
        print("{:2d}. {:10.2f} euroa".format(i, paaoma))


def main():
    print("Ohjelma laskee sijoituksen arvon kehittymisen vuosittain")
    rivi = input("Anna sijoitettava summa (euroa): ")
    summa = float(rivi)
    rivi = input("Anna sijoitusaika (vuotta): ")
    vuodet = int(rivi)
    rivi = input("Anna odotettu tuottoprosentti: ")
    tuotto = float(rivi)
    laske_arvokehitys(summa, vuodet, tuotto)


main()