'''
Player 1, enter your choice (R/P/S): P
Player 2, enter your choice (R/P/S): S
Player 2 won!
'''


def main():
    player1 = input("Player 1, enter your choice (R/P/S): ")
    player2 = input("Player 2, enter your choice (R/P/S): ")

    if player1 == player2:
        print("It's a tie!")
    elif player1 == "R":
        if player2 == "S":
            print("Player 1 won!")
        elif player2 == "P":
            print("Player 2 won!")
    elif player1 == "P":
        if player2 == "R":
            print("Player 1 won!")
        elif player2 == "S":
            print("Player 2 won!")
    elif player1 == "S":
        if player2 == "R":
            print("Player 2 won!")
        if player2 == "P":
            print("Player 1 won!")


main()
