def main():
    i = 0
    syote = input("How many numbers would you like to have? ")
    lukuja = int(syote)
    for i  in range(lukuja):
        i += 1
        if i % 3 == 0 and i % 7 == 0:
            print("zip boing")
        elif i % 7 == 0:
            print("boing")
        elif i % 3 == 0:
            print("zip")
        else:
            print(i)


main()