# TIE-02100 Johdatus ohjelmointiin
# Read genres and tv-series from a file into a dict.
# Print a list of the genres in alphabetical order
# and list tv-series by given genre on user's command.


def read_file(filename):
    # reads and saves the series and their genres from the file

    movies_by_genre = {}
    all_genres = []

    try:
        file = open(filename, "r")

        for row in file:
            name, genres = row.rstrip().split(";")
            genres = genres.split(",")

            for genre in genres:
                if genre in movies_by_genre:
                    movies_by_genre[genre].append(name)
                else:
                    movies_by_genre[genre] = [name]

            for genre in genres:
                if genre not in all_genres:
                    all_genres.append(genre)
            all_genres = sorted(all_genres)

        file.close()

        return movies_by_genre, all_genres

    except ValueError:
        print("Error: rows were not in the format name;genres.")
        return None

    except IOError:
        print("Error: the file could not be read.")
        return None


def main():

    filename = input("Enter the name of the file: ")
    #filename = "series.txt"

    data = read_file(filename)
    movies_by_genre = data[0]
    all_genres = data[1]

    print("Available genres are: {}".format(", ".join(all_genres)))

    while True:
        genre = input("> ")

        if genre == "exit":
            return

        if genre in movies_by_genre:
            for movie in sorted(movies_by_genre[genre]):
                print(movie)

main()
