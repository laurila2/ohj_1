# Python program to convert
# JSON file to CSV

import csv
import json


def lue_tiedosto(fileinput, fileoutput):
    try:
        with open(fileinput) as json_file:
            data = json.load(json_file)

        data_file = open(fileoutput, "w")

        csv.register_dialect(
            'mydialect',
            delimiter=';',
            quotechar='"',
            doublequote=True,
            skipinitialspace=True,
            lineterminator='\r',
            quoting=csv.QUOTE_MINIMAL)

        csv_writer = csv.writer(data_file, dialect='mydialect')

        for station in data:
            csv_writer.writerow((station["stationId"], station["name"]))
        data_file.close()
        return True
    except (OSError, IndexError):
        print("There was an error in handling the file.")
        return False

def main():
    fileInput = input("Enter the name of the input file: ")
    fileOutput = input("Enter the name of the output file: ")
    # fileInput = "small_data.json"
    # fileOutput = "tulos2.csv"

    luku_onnistui = True

    luku_onnistui = lue_tiedosto(fileInput, fileOutput)

    if not luku_onnistui:
        return
    if luku_onnistui:
        print("")
        print("Conversion succeeded.")


main()
