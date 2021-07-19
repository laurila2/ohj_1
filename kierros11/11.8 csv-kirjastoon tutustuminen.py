import csv

def main():

    filename = input("Enter the name of the input file: ")
    tyyppi = input("and its dialect: ")

    output_file = input("Enter the name of the output file: ")
    output_tyyppi = input("and its dialect: ")

    try:
        with open(filename, "r", newline='') as file:
            reader = csv.reader(file, dialect=tyyppi)
            with open(output_file, "w", newline='') as file2:
                writer = csv.writer(file2, dialect=output_tyyppi)
                writer.writerows(reader)

        print("")
        print(f"File {filename} has been converted into {output_tyyppi}.")

    except IOError:
        print("")
        print("There was an error in handling the file.")
    except csv.Error:
        print("")
        print("The given dialect is wrong.")


main()
