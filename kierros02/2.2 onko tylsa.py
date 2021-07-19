def main():

    rivi = input("Answer Y or N: ")
    tila = str(rivi)

    found = False
    while not found:
        if tila.lower() in ('y', 'n'):
            found = True
        else:
            print("Incorrect entry.")
            rivi = input("Please retry: ")
            tila = str(rivi)
    print("You answered ", tila)


main()
