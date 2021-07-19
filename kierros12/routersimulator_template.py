class Router:

    def __init__(self, name):
        """
        Constructor. Initializes router's name.
        :param name: router's name
        """

        self.__name = name
        self.__neighbours = []
        self.__routing_table = {}

    def add_neighbour(self, other_router):
        self.__neighbours.append(other_router.__name)

    def add_network(self, address, distance):
        self.__routing_table[address] = int(distance)

    def has_route(self, network_name):
        if network_name in self.__routing_table:
            if self.__routing_table[network_name] == 0:
                print("Router is an edge router for the network.")
            elif 1 <= self.__routing_table[network_name] <= 5:
                print(f"Network {network_name} is "
                      f"{self.__routing_table[network_name]} hops away")
        else:
            print("Route to the network is unknown.")

    def receive_routing_table(self, other_router):
        for osoite in other_router.__routing_table:
            if osoite not in self.__routing_table:
                self.__routing_table[osoite] = \
                    other_router.__routing_table[osoite] + 1

    def get_neighbours(self):
        neighbours = self.__neighbours
        return neighbours

    def print_info(self):
        lista = []
        if len(self.__routing_table) > 0:
            for key, value in self.__routing_table.items():
                lista.append(f"{key}:{value}")
            lista = sorted(lista)
            address = ", ".join(lista)
        else:
            address = ""

        self.__neighbours = sorted(self.__neighbours)
        neighbours = ", ".join(self.__neighbours)
        print(" ", self.__name)
        print("    N:", neighbours)
        print("    R:", address)

def lue_tiedosto(routerfile, routers):
    try:
        file = open(routerfile, "r")
        for row in file:
            rivi = row.rstrip().split("!")

            name = rivi[0]
            neighbours = rivi[1]
            network = rivi[2]

            if name not in routers:
                router = Router(name)
                routers[name] = router

            if len(neighbours) >= 1:
                neighbours = neighbours.split(";")
                for neighbour in neighbours:
                    if neighbour not in routers:
                        routers[neighbour] = Router(neighbour)
                    routers[name].add_neighbour(routers[neighbour])

            if len(network) >= 1:
                networks = network.split(";")
                for network in networks:
                    network = network.split(":")
                    routers[name].add_network(network[0], network[1])
        file.close()
        return True

    except (OSError, IndexError):
        print("Error: the file could not be read or there "
              "is something wrong with it.")
        return False

def main():

    routers = {}
    routerfile = input("Network file: ")

    luku_onnistui = True

    if routerfile != "":
        luku_onnistui = lue_tiedosto(routerfile, routers)
    if not luku_onnistui:
        return

    while True:
        command = input("> ")
        command = command.upper()

        if command == "P":
            name = input("Enter router name: ")
            if name in routers:
                routers[name].print_info()
            else:
                print("Router was not found.")

        elif command == "PA":
            for name in routers:
                routers[name].print_info()

        elif command == "S":
            name = input("Sending router: ")
            if name in routers:
                neighbours = routers[name].get_neighbours()
                for neighbour in neighbours:
                    routers[neighbour].receive_routing_table(routers[name])
            else:
                print("Router was not found.")

        elif command == "C":
            name1 = input("Enter 1st router: ")
            name2 = input("Enter 2nd router: ")

            if name1 and name2 in routers:
                routers[name1].add_neighbour(routers[name2])
                routers[name2].add_neighbour(routers[name1])

        elif command == "RR":
            name = input("Enter router name: ")
            network = input("Enter network name: ")

            if name in routers:
                routers[name].has_route(network)

        elif command == "NR":
            name = input("Enter a new name: ")

            if name in routers:
                print("Name is taken.")
            else:
                router = Router(name)
                routers[name] = router

        elif command == "NN":
            name = input("Enter router name: ")
            address = input("Enter network: ")
            distance = input("Enter distance: ")

            if name in routers:
                routers[name].add_network(address, distance)

        elif command == "Q":
            print("Simulator closes.")
            return

        else:
            print("Erroneous command!")
            print("Enter one of these commands:")
            print("NR (new router)")
            print("P (print)")  
            print("C (connect)")
            print("NN (new network)")
            print("PA (print all)")
            print("S (send routing tables)")
            print("RR (route request)")
            print("Q (quit)")


main()
