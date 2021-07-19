def main():
    print("Lasken keskiarvon antamistasi kokonaisluvuista.")
    rivi = input("Anna lukujen maara: ")
    lukujen_maara = int(rivi)
    i = 0
    summa = 0
    while i < lukujen_maara:
        rivi = input("Anna seuraava luku: ")
        luku = int(rivi)
        summa = summa + luku
        i = i + 1
    if lukujen_maara > 0:
        keskiarvo = summa / lukujen_maara
        print("Niiden keskiarvo on", keskiarvo)
    else:
        print("Et antanut yhtaan lukua.")

main()