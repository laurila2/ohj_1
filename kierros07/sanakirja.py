def main():
    english_spanish = {"hey": "hola", "thanks": "gracias", "home": "casa"}

    while True:
        command = input("[W]ord/[A]dd/[R]emove/[P]rint/[T]ranslate/[Q]uit: ")

        if command == "W":
            word = input("Enter the word to be translated: ")
            if word in english_spanish:
                print(word, "in Spanish is", english_spanish[word])
            else:
                print("The word", word,
                      "could not be found from the dictionary.")

        elif command == "A":
            eng_word = input("Give the word to be added in English: ")
            spanish_word = input("Give the word to be added in Spanish: ")
            english_spanish[eng_word] = spanish_word

        elif command == "R":
            word = input("Give the word to be removed: ")
            if word in english_spanish:
                del english_spanish[word]
            else:
                print("The word", word,
                      "could not be found from the dictionary.")

        elif command == "P":
            for word in sorted(english_spanish):
                print("{} {}".format(word, english_spanish[word]))

        elif command == "T":
            translate = []
            rivi = input("Enter the text to be translated into Spanish: ")
            translate = rivi.split()
            text = ""

            for word in translate:
                if word in english_spanish:
                    text += english_spanish[word] + " "
                else:
                    text += word + " "

            print("The text, translated by the dictionary:")
            print(text)

        elif command == "Q":
            print("Adios!")
            return

        else:
            print("Unknown command, enter W, A, R, P, T or Q!")


main()
