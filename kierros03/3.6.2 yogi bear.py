# TIE-02100 Johdatus ohjelmointiin
# Koodipohja laulu c, Yogi Bear

def repeat_name(etunimi, toistot):
    for i in range(toistot):
        print("{}, {} Bear".format(etunimi, etunimi))


def verse(sae, etunimi):
    print(sae)
    print("{}, {}".format(etunimi, etunimi))
    print(sae)
    repeat_name(etunimi, 3)
    print(sae)
    print("{}, {} Bear".format(etunimi, etunimi))
    print("")


def main():
    verse("I know someone you don't know", "Yogi")
    verse("Yogi has a best friend too", "Boo Boo")
    verse("Yogi has a sweet girlfriend", "Cindy")


main()
