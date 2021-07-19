"""
TIE-02101 Ohjelmointi 1 / TIE-02107 Programming 1
Santeri Laurila
"""

DEFAULT_FILENAME = "products.txt"


def find_cheapest_stores(data):
    kaupat = data[0]
    tuotteet = data[1]

    basket = read_shopping_basket()

    alin_hinta = 10000
    for kauppa in kaupat:
        hinta = calculate_basket_price(kaupat[kauppa], basket)
        if hinta < alin_hinta:
            alin_hinta = hinta

    print(alin_hinta)
    print(basket)


def print_known_products(data):
    tuotteet = data[1]

    print("Available products:")
    for tuote in sorted(tuotteet):
        print_price_info(tuote, tuotteet[tuote])


def print_selections(data):
    kaupat = data[0]
    tuotteet = data[1]

    for kauppa in sorted(kaupat):
        print(kauppa)
        for tuote in sorted(kaupat[kauppa]):
            print_price_info(tuote, kaupat[kauppa][tuote])


def read_inputfile(filename):
    kaupat = {}
    tuotteet = {}

    try:
        tiedosto = open(filename, "r")
        rivilista = tiedosto.readlines()
        tiedosto.close()

        for rivi in rivilista:
            rivi = rivi.rstrip()
            tiedot = rivi.split(":")

            kauppa = tiedot[0]
            tuote = tiedot[1]
            hinta = tiedot[2]

            if kauppa not in kaupat:
                kaupat[kauppa] = {}

            kaupat[kauppa][tuote] = float(hinta)

            # sanakirja tuoteet ja sen halvin hinta
            if tuote not in tuotteet:
                tuotteet[tuote] = float(hinta)
            elif float(hinta) < float(tuotteet[tuote]):
                tuotteet[tuote] = float(hinta)

    except OSError:
        print(f"Error: file {filename} cannot be read.")

    return kaupat, tuotteet


def print_price_info(product, price):
    print("    {:<15s} {:>10.2f} e".format(product, float(price)))


def read_shopping_basket():
    print("Input product names separated by a white space:")
    syote = input()
    products = syote.split(" ")

    # palauttaa tuotteet listana
    return products


def calculate_basket_price(selection, basket):
    """
    This function is used to calculate the total price of the
    content of the shopping basket for a particular store.

    Parameters:
        selection:
            A data structure containing information about all the
            products and their prices in one store. Could possibly be
            implemented as a dict with product name as a key and
            price as a payload.

        basket:
            A data structure containing all the items a customer
            has collected in their shopping basket. Could possibly be
            implemented as a list of strings.

    Return value:
        The price of the shopping basket (float) or None if
        the store's selection of products doesn't include all the
        items in the basket.
    """

    price = 0.00
    for product in basket:
        if product in selection:
            price += selection[product][price]

    return price


def main():
    data = read_inputfile(DEFAULT_FILENAME)

    print("Welcome to the shopping basket optimization app!")
    print("Available commands:")
    print(" S Print all the [S]tores with their available products")
    print(" P Print all the [P]roducts available in all the stores")
    print(" C Show the [C]heapest seller for a specified shopping basket")
    print(" Q [Q]uit")

    while True:
        print()

        command = input("Input command (S, P, C, Q): ")

        if command == "S":
            print_selections(data)

        elif command == "P":
            print_known_products(data)

        elif command == "C":
            find_cheapest_stores(data)

        elif command == "Q":
            print("Bye!")
            return

        else:
            print("Unknown command!?!")


main()
