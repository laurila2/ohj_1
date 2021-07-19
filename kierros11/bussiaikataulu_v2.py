# TIE-02100 Johdatus ohjelmointiin
# Esimerkki: kellonaikaluokan toteutus

class Kellonaika:

    def __init__(self, hh = 0, mm = 0):
        self.__hh = hh
        self.__mm = mm

    def __str__(self):
        return str(self.__hh) + ":" + str(self.__mm).rjust(2, '0')

    # Palauttaa tiedon siitä, kuinka monta minuuttia kellonaika on keskiyöstä
    def __int__(self):
        return self.__mm + self.__hh*60

    def ero_minuutteina(self, kellonaika):
        return int(kellonaika) - int(self)

    def __sub__(self, kellonaika):
        ero_minuutteina = int(kellonaika) - int(self)

        tunnit = ero_minuutteina // 60
        minuutit = ero_minuutteina % 60

        erotus = Kellonaika(tunnit, minuutit)
        return erotus

    def __lt__(self, kellonaika):
        return self.ero_minuutteina(kellonaika) > 0


def main():
    aikataulu = [Kellonaika(6, 30), Kellonaika(10, 15), Kellonaika(14, 15),
                 Kellonaika(16, 20), Kellonaika(17, 20), Kellonaika(20)]

    tuntilukema = int(input("Syötä kellonajan tuntilukema: "))
    minuuttilukema = int(input("Syötä kellonajan minuuttilukema: "))

    kellonaika_nyt = Kellonaika(tuntilukema, minuuttilukema)

    for aika in aikataulu:
        if kellonaika_nyt < aika:
            print("Seuraava bussi lähtee:", aika)
            print("Lähtöön on aikaa:", kellonaika_nyt - aika)
            return

    print("Tänään ei enää mene busseja!")


main()
