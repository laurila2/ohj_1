
def main():

    rivi = input("Choose a number: ")
    luku = int(rivi)
    tulos = int(1)

    i = 1

    while tulos < 100:
        tulos = i * luku
        print(i ,"*", luku, "=", i * luku)
        i = i + 1


main()
