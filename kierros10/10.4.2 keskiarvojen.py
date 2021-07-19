def read_file(filename):

    ovens = []

    try:
        file = open(filename, "r")

        real_time = 0
        edellinen_aikaleima = 0
        uuni1_vanha = 0
        uuni2_vanha = 0
        uuni3_vanha = 0

        for row in file:
            time, uuni1, uuni2, uuni3 = row.rstrip().split(";")
            time = str(time)

            if time != "Time":
                uuni1 = uuni1.split(",")
                if len(uuni1) == 2:
                    uuni1 = uuni1[0] + "." + uuni1[1]
                    uuni1 = float(uuni1)
                else:
                    uuni1 = float(uuni1[0])

                uuni2 = uuni2.split(",")
                if len(uuni2) == 2:
                    uuni2 = uuni2[0] + "." + uuni2[1]
                    uuni2 = float(uuni2)
                else:
                    uuni2 = float(uuni2[0])

                uuni3 = uuni3.split(",")
                if len(uuni3) == 2:
                    uuni3 = uuni3[0] + "." + uuni3[1]
                    uuni3 = float(uuni3)
                else:
                    uuni3 = float(uuni3[0])

                h, m, s = time.split(":")
                aikaleima = int(h) * 3600 + int(m) * 60 + int(s)

                if edellinen_aikaleima != 0:
                    delta = aikaleima - edellinen_aikaleima
                    uuni1_d = (uuni1 - uuni1_vanha) / delta
                    uuni2_d = (uuni2 - uuni2_vanha) / delta
                    uuni3_d = (uuni3 - uuni3_vanha) / delta

                    ovens.append(["{:.1f}".format(delta), "{:.1f}".format(uuni1_d),
                                  "{:.1f}".format(uuni2_d), "{:.1f}".format(uuni3_d)])

                if aikaleima < real_time:
                    aikaleima += 86400

                real_time = aikaleima
                edellinen_aikaleima = aikaleima
                uuni1_vanha = uuni1
                uuni2_vanha = uuni2
                uuni3_vanha = uuni3

        file.close()

    except IOError:
        print("There was an error in reading the file!")

    return ovens

def write_file(ovens, filename):

    file = open(filename, "a")

    for i in ovens:
        row = "{};{};{};{}\n".format(i[0], i[1], i[2], i[3])
        file.write(row)
    file.close()

    print("Information saved successfully.")

def main():

    filename = input("Enter the name of the file: ")
    new_file = input("Enter the name of the file to be written: ")

    #filename = "ovendata.csv"
    #new_file = "ovendata_changes.csv"

    data = read_file(filename)
    write_file(data, new_file)



main()
