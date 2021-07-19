# Tämä ohjelma laskee Fibonacci-sarjan
def hae_fibo(n):
    if n <= 1:
        return n
    else:
        return (hae_fibo(n - 1) + hae_fibo(n - 2))

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