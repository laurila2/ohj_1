# How do you feel? (1-10) 6
# A suitable smiley would be :-|


def main():
    rivi = input("How do you feel? (1-10) ")
    mielentila = int(rivi)

    if mielentila == 10:
        print("A suitable smiley would be :-D")
    elif 7 < mielentila <= 9:
        print("A suitable smiley would be :-)")
    elif 4 <= mielentila <= 7:
        print("A suitable smiley would be :-|")
    elif 2 <= mielentila < 4:
        print("A suitable smiley would be :-(")
    elif mielentila == 1:
        print("A suitable smiley would be :'(")
    else:
        print("Bad input!")

main()
