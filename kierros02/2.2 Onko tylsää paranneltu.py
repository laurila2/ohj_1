
def main():

    tila = "n"
    found = False

    while tila == "n":
        rivi = input("Bored? (y/n) ")
        tila = str(rivi)
        while not found:
            if tila.lower() in ('y', 'n'):
                found = True
            else:
                print("Incorrect entry.")
                rivi = input("Please retry: ")
                tila = str(rivi)
    print("Well, let's stop this, then.")

main()
