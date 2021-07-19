paalla = True

while paalla == True:
    syote = input("laita numero: ")
    uusi_numero = int(syote)
    try:
        if abs(uusi_numero - temp) > 2:
            print("Ero on suurempi kuin 2")
            paalla = False
    except NameError:
        temp = uusi_numero
        continue
