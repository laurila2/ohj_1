# Introduction to Programming spring 2020
# Geometriset kuviot -tehtävä
# Santeri Laurila

import math
PI = math.pi

def syotteen_tarkastus(fraasi):
    # Tarkistaa, että käyttäjä on syöttänyt positiivisen arvon
    sivu = float(input(fraasi))

    while sivu < 0.01:
        sivu = float(input(fraasi))
    return sivu

def nelio():
    # Laskee neliön piirin ja pinta-alan
    side = syotteen_tarkastus("Enter the length of the square's side: ")
    circumference = side * 4
    square_area = side ** 2
    print("The total circumference is {:.2f}".format(circumference))
    print("The surface area is {:.2f}".format(square_area))

def suorakaide():
    # Laskee suorakaiteen piirin ja pinta-alan
    sivu1 = syotteen_tarkastus("Enter the length of the rectangle's side 1: ")
    sivu2 = syotteen_tarkastus("Enter the length of the rectangle's side 2: ")
    circumference_rectangle = sivu1 * 2 + sivu2 * 2
    rectangle_area = sivu1 * sivu2
    print("The total circumference is {:.2f}".format(circumference_rectangle))
    print("The surface area is {:.2f}".format(rectangle_area))

def ympyra():
    radius = syotteen_tarkastus("Enter the circle's radius: ")
    circumference = 2 * PI * radius
    area = PI * radius ** 2
    print("The total circumference is {:.2f}".format(circumference))
    print("The surface area is {:.2f}".format(area))

def menu():
    # Kysyy käyttäjältä, mikä kuvio valitaan
    while True:
        answer = input("Enter the pattern's first letter, q stops this (s/r/q): ")

        if answer == "s":
            nelio()

        elif answer == "r":
            suorakaide()

        elif answer == "c":
            ympyra()

        elif answer == "q":
            return

        else:
            print("Incorrect entry, try again!")

        print()  # Empty row for the sake of readability


def main():
    menu()
    print("Goodbye!")


main()