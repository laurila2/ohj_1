
def main():

    rivi = input("Bored? (y/n) ")
    tila = str(rivi)

    while tila == "n":
        rivi = input("Bored? (y/n) ")
        tila = str(rivi)
    print("Well, let's stop this, then.")

main()
