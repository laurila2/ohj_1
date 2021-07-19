"""
TIE-0210X
Mölkky
Santeri Laurila
"""

class Player:
    def __init__(self, nimi):
        self.__playername = nimi
        self.__playerscore = 0
        self.__playerthrows = 0
        self.__player__totalpoints = 0
        self.__player_throwsthathit = 0

    def get_name(self):
        return self.__playername

    def get_points(self):
        return self.__playerscore

    def has_won(self):
        if self.__playerscore == 50:
            return True
        else:
            return False

    def add_points(self, points):
        self.__playerscore += points
        self.__playerthrows += 1
        self.__player__totalpoints += points

        if points > 0:
            self.__player_throwsthathit += 1

        if self.__playerscore > 50:
            print(f"{self.__playername} gets penalty points!")
            self.__playerscore = 25
        elif 40 <= self.__playerscore <= 49:
            pts_puuttuu = 50 - self.__playerscore
            print(f"{self.__playername} needs only {pts_puuttuu} points. "
                  f"It's better to avoid knocking "
                  f"down the pins with higher points.")

        return self.__playerscore

    def cheer(self, points):
        if self.__playerthrows >= 1:
            average = self.__player__totalpoints / self.__playerthrows
            if points > average:
                print(f"Cheers {self.__playername}!")

    def accuracy(self):
        if self.__playerthrows > 0:
            hit_percentage = (self.__player_throwsthathit /
                              self.__playerthrows) * 100
            return hit_percentage
        else:
            return 0.0


def main():

    player1 = Player("Matti")
    player2 = Player("Teppo")

    throw = 1
    while True:
        if throw % 2 == 0:
            in_turn = player1
        else:
            in_turn = player2

        pts = int(input("Enter the score of player " + in_turn.get_name() +
                        " of throw " + str(throw) + ": "))
        
        in_turn.add_points(pts)
        in_turn.cheer(pts)
                        
        if in_turn.has_won():
            print("Game over! The winner is " + in_turn.get_name() + "!")
            return

        print("")
        print("Scoreboard after throw " + str(throw) + ":")
        print(player1.get_name() + ":", player1.get_points(),
              "p, hit percentage {:.1f}".format(player1.accuracy()))
        print(player2.get_name() + ":", player2.get_points(),
              "p, hit percentage {:.1f}".format(player2.accuracy()))
        print("")

        throw += 1


main()
