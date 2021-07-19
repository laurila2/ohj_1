# TIE-02100 Johdatus ohjelmointiin
# Esimerkki: vieterilelusammakon toteuttaminen luokkana

class Sammakko:
    def __init__(self, jousen_koko):
        self.__jousen_jännitys = 0
        self.__maksimijännitys = jousen_koko

    def ruuvaa(self):
        # Jos sammakon jousi on jo rikki, niin mitään ei tapahdu
        if self.__maksimijännitys is None:
            return

        self.__jousen_jännitys += 1
        if self.__jousen_jännitys <= self.__maksimijännitys:
            # Jos jousta pystyy vielä jännittämään niin kuuluu normaali ääni
            print("skriik")
        else:
            # Jos jousi jännitetään yli, niin se rikkoutuu ja kuuluu
            # rikkoutumisääni
            print("kräks!")
            self.__maksimijännitys = None


    def hyppää(self):
        # Jos sammakon jousi on jo rikki, niin mitään ei tapahdu
        if self.__maksimijännitys is None:
            return

        for i in range(self.__jousen_jännitys, 0, -1):
            if i > 3:
                print("boing ", end="")
            elif i > 1:
                print("boooing ", end="")
            else:
                print("boooo...")
        print()
        self.__jousen_jännitys = 0


def main():

    saku = Sammakko(8)
    saku.hyppää()

    for i in range(8):
        saku.ruuvaa()

    saku.hyppää()


main()
