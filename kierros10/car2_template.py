# TIE-02100 Johdatus ohjelmointiin

MENU_TEXT = "1) Fill 2) Drive 3) Quit\n-> "
CAR_TEXT = "The tank contains {:.1f} liters of gas and " + \
           "the odometer shows {:.1f} kilometers."


# Class Car: Implements a car that moves a certain distance and can be
# filled. The class defines what is the car like: what information it
# contains and what operations can be carried out for it.
class Car:

    # Method: constructor, initiates the object (tank is empty and
    # location is 0, 0)
    # Parameter: tank_size, the size of this car's tank
    # Parameter: gas_consumption, how much gas this car consumes when it
    #            drives a 100 kilometers
    def __init__(self, tank_size, gas_consumption):
        self.__tank_size = tank_size
        self.__gas_consumption = gas_consumption
        self.__gas = 0.0
        self.__odometer = 0.0

    def printInformation(self):
        print(CAR_TEXT.format(self.__gas, self.__odometer))

    def fill(self, new_gas):
        if new_gas < 0:
            print("You cannot remove gas from the tank")
            return

        if (self.__gas + new_gas) <= self.__tank_size:
            self.__gas = self.__gas + new_gas
        else:
            self.__gas = self.__tank_size

    def drive(self, matka):

        if matka < 0:
            print("You cannot travel a negative distance")
            return

        kulutus = matka * (self.__gas_consumption / 100)

        if (self.__gas - kulutus) >= 0.0:
            self.__odometer += matka
            self.__gas -= kulutus
        else:
            # ajetaan tankki tyhjäksi
            ajettu_matka = (self.__gas / self.__gas_consumption) * 100
            self.__odometer += ajettu_matka
            self.__gas = 0

            return


def read_number(prompt, error_message="Incorrect input!"):
    # This function reads input from the user.
    try:
        return float(input(prompt))
    except ValueError:
        print(error_message)
        return read_number(prompt, error_message)


def main():
    tank_size = read_number("How much does the vehicle's gas tank hold? ")
    gas_consumption = read_number("How many liters of gas does the car "
                                  "consume per hundred kilometers? ")

    car = Car(tank_size, gas_consumption)

    while True:
        car.printInformation()
        choice = input(MENU_TEXT)

        if choice == "1":
            to_fill = read_number("How many liters of gas to fill up? ")
            car.fill(to_fill)
        elif choice == "2":
            distance = read_number("How many kilometers to drive? ")
            car.drive(distance)
        elif choice == "3":
            break

    print("Thank you and bye!")


main()
