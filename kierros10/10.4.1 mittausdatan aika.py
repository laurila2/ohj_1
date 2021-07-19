def read_file(filename):

    ovens = {}

    try:
        file = open(filename, "r")

        real_time = 0
        for row in file:
            time, uuni1, uuni2, uuni3 = row.rstrip().split(";")
            time = str(time)

            if time != "Time":
                h, m, s = time.split(":")
                aikaleima = int(h) * 3600 + int(m) * 60 + int(s)

                if aikaleima < real_time:
                    aikaleima += 86400

                ovens[aikaleima] = [uuni1, uuni2, uuni3]
                real_time = aikaleima
        file.close()

    except (IOError, ValueError):
        print("There was an error in reading the file!")

    return ovens

def write_file(ovens, filename):

    file = open(filename, "a")
    file.write("Time;°C(1)K;°C(2)K;°C(3)K\n")

    for key in ovens:
        file.write(f"{key};{ovens[key][0]};{ovens[key][1]};{ovens[key][2]}\n")
    file.close()

def main():

    filename = input("Enter the name of the file: ")
    new_file = input("Enter the name of the file to be written: ")

    data = read_file(filename)
    write_file(data, new_file)


main()
