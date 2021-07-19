# Tämä ohjelma laskee Fibonacci-sarjan
def erotus(luku1, luku2):
    if luku1 and luku2 <= 1:
        return n
    else:
        return luku1 - luku2

def main():
    syote = input("How many Fibonacci numbers do you want? ")
    lukuja = int(syote)

    # tarkistus, että syöte on oikeanlainen
    if lukuja <= 0:
        print("Plese enter a positive integer")
    else:
        for i in range(1, lukuja + 1):
            print(i, ". ", hae_fibo(i), sep="")


main()