class Fraction:
    """ This class represents one single fraction that consists of
        numerator and denominator """

    def __init__(self, numerator, denominator):
        """
        Constructor. Checks that the numerator and denominator are of
        correct type and initializes them.

        :param numerator: fraction's numerator
        :param denominator: fraction's denominator
        """

        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise TypeError
        elif denominator == 0:
            raise ValueError

        self.__numerator = numerator
        self.__denominator = denominator

    def __lt__(self, fraction):
        new_num1 = self.__numerator * fraction.__denominator
        new_num2 = fraction.__numerator * self.__denominator

        if new_num1 < new_num2:
            return True
        else:
            return False

    def __gt__(self, fraction):
        new_num1 = self.__numerator * fraction.__denominator
        new_num2 = fraction.__numerator * self.__denominator

        if new_num1 > new_num2:
            return True
        else:
            return False

    def __str__(self):
        return self.return_string()

    def return_string(self):
        """ Returns a string-presentation of the fraction in the format
        numerator/denominator """

        if self.__numerator * self.__denominator < 0:
            sign = "-"
        else:
            sign = ""
        return "{:s}{:d}/{:d}".format(sign, abs(self.__numerator),
                                      abs(self.__denominator))

    def simplify(self):
        tekija = greatest_common_divisor(self.__numerator, self.__denominator)
        self.__numerator = self.__numerator // tekija
        self.__denominator = self.__denominator // tekija

    def complement(self):
        if self.__numerator * self.__denominator < 0:
            new_num = abs(self.__numerator)
            new_denom = abs(self.__denominator)
            return Fraction(new_num, new_denom)
        else:
            new_num = -1 * self.__numerator
            new_denom = self.__denominator
            return Fraction(new_num, new_denom)

    def reciprocal(self):
        return Fraction(self.__denominator, self.__numerator)

    def multiply(self, fraction):
        new_num = self.__numerator * fraction.__numerator
        new_denom = self.__denominator * fraction.__denominator

        multiply = Fraction(new_num, new_denom)
        return multiply

    def divide(self, fraction):
        new_num = self.__numerator * fraction.__denominator
        new_denom = self.__denominator * fraction.__numerator

        divide = Fraction(new_num, new_denom)
        return divide

    def add(self, fraction):
        new_num = self.__numerator * fraction.__denominator \
                  + fraction.__numerator * self.__denominator
        new_denom = self.__denominator * fraction.__denominator
        add = Fraction(new_num, new_denom)

        return add

    def deduct(self, fraction):
        new_num = self.__numerator * fraction.__denominator \
                  - fraction.__numerator * self.__denominator
        new_denom = self.__denominator * fraction.__denominator
        deduct = Fraction(new_num, new_denom)

        return deduct

def greatest_common_divisor(a, b):
    """
    Euclidean algorithm.
    """

    while b != 0:
        a, b = b, a % b
    return a

def add(murtoluvut):
    rivi = input("Enter a fraction in the form integer/integer: ")
    name = input("Enter a name: ")

    luku = rivi.split("/")
    osoittaja = int(luku[0])
    nimittaja = int(luku[1])

    frac = Fraction(osoittaja, nimittaja)
    murtoluvut[name] = frac

def main():

    murtoluvut = {}

    while True:
        rivi = input("> ")

        if rivi == "quit":
            print("Bye bye!")
            break

        elif rivi == "add":
            add(murtoluvut)

        elif rivi == "print":
            name = input("Enter a name: ")
            if name in murtoluvut:
                print(f"{name} = {murtoluvut[name].return_string()}")
            else:
                print(f"Name {name} was not found")

        elif rivi == "list":
            if len(murtoluvut) >= 1:
                for name in sorted(murtoluvut):
                    print(f"{name} = {murtoluvut[name].return_string()}")

        elif rivi == "*":
            name1 = input("1st operand: ")
            if name1 not in murtoluvut:
                print(f"Name {name1} was not found")

            if name1 in murtoluvut:
                name2 = input("2nd operand: ")
                if name2 not in murtoluvut:
                    print(f"Name {name2} was not found")

            if name1 and name2 in murtoluvut:
                frac = murtoluvut[name1].multiply(murtoluvut[name2])
                print(f"{murtoluvut[name1]} * {murtoluvut[name2]} = "
                      f"{frac.return_string()}")
                frac.simplify()
                print(f"simplified {frac.return_string()}")

        elif rivi == "file":
            filename = input("Enter the name of the file: ")
            # filename = "fractions.txt"
            try:
                file = open(filename, "r")
                for row in file:
                    rivi = row.rstrip().split("=")

                    luku = rivi[1].split("/")
                    osoittaja = int(luku[0])
                    nimittaja = int(luku[1])

                    frac = Fraction(osoittaja, nimittaja)
                    murtoluvut[rivi[0]] = frac

            except (OSError, IndexError):
                print("Error: the file cannot be read.")
        else:
            print("Unknown command!")


main()
