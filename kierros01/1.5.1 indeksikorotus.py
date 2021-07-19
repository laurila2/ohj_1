'''
Enter the amount of the study benefits: 335.32
If the index raise is 1.17 percent, the study benefit,
after a raise, would be 339.243244 euros
'''


def main():
    rivi = input("Enter the amount of the study benefits: ")

    opintotuki = float(rivi)
    korotus = 1.0117
    korotettu_tuki = korotus * opintotuki

    print("If the index raise is 1.17 percent, the study benefit,")
    print("after a raise, would be", korotettu_tuki, "euros")

    print("and if there was another index raise, the study")
    print("benefits would be as much as", korotettu_tuki * korotus, "euros")


main()
