

def main():
    rivi = input("Purchase price: ")
    hinta = int(rivi)
    rivi = input("Paid amount of money: ")
    maksettu = int(rivi)

    vaihtorahat = maksettu - hinta

    kympit = vaihtorahat // 10
    jaannoseurot = vaihtorahat % 10
    print("jaannoseurot: ", jaannoseurot)
    vitoset = jaannoseurot // 5
    jaannoseurot = vaihtorahat % 5
    kakkoset = jaannoseurot // 2
    jaannoseurot = vaihtorahat % 2
    eurot = jaannoseurot // 1
    jaannoseurot = vaihtorahat % 1
    eurot = jaannoseurot


    if (vaihtorahat) > 0:
        print("Offer change: ", vaihtorahat)
        if kympit > 0:
            print(kympit, " ten-euro notes")
        if vitoset > 0:
            print(vitoset, " five-euro notes")
        if kakkoset > 0:
            print(kakkoset, " two-euro coins")
        if eurot > 0:
            print(eurot, " one-euro coins")
    else:
        print("No change")


main()
