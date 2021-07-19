# Akvaariokalat vaativat vedeltä  6.0 - 8.0 pH:n tason.

def main():
    syote = input("Enter the number of the measurements: ")
    mittausten_lkm = int(syote)
    i = 0

    if mittausten_lkm < 1:
        print("Error: the number must be expressed as a positive integer.")
    else:
        summa = 0
        while i < mittausten_lkm:
            syote = input("Enter the measurement result %s: " % (i + 1))
            mittaustulos = float(syote)
            i += 1
            summa = summa + mittaustulos
            keskiarvo = summa / mittausten_lkm

            try:
                if mittaustulos < 6.0 or mittaustulos > 8.0 or abs(mittaustulos - temp) > 1:
                    print("The conditions are not suitable for zebra fishes.")
                    break
            except NameError:
                continue
            temp = mittaustulos

        if 6.0 < keskiarvo < 8.0:
            print("Conditions are suitable for zebra fishes. The average pH is %.2f." % keskiarvo)


main()
