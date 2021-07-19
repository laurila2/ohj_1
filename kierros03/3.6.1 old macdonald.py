# TIE-02100 Johdatus ohjelmointiin
# TIE-02100 Introduction to programming
# Template song b, Old MacDonald

def print_verse(elain, aani):
    print("Old MACDONALD had a farm")
    print("E-I-E-I-O")
    print("And on his farm he had a {}".format(elain))
    print("E-I-E-I-O")
    print("With a {} {} here".format(aani, aani))
    print("And a {} {} there".format(aani, aani))
    print("Here a {}, there a {}".format(aani, aani))
    print("Everywhere a {} {}".format(aani, aani))
    print("Old MacDonald had a farm")
    print("E-I-E-I-O")
    print()


def main():
    print_verse("cow", "moo")
    print_verse("pig", "oink")
    print_verse("duck", "quack")
    print_verse("horse", "neigh")
    print_verse("lamb", "baa")


main()
