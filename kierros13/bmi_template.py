# TIE-02100 Johdatus ohjelmointiin
# BMI

from tkinter import *

NAN = float("NaN")

class Userinterface:
    def __init__(self):
        self.__mainwindow = Tk()
        self.__mainwindow.title("BMI calculator")

        self.__weight_text = Label(self.__mainwindow, text="Weight (kg):")
        self.__height_text = Label(self.__mainwindow, text="Height (cm):")

        self.__weight_value = Entry(self.__mainwindow)
        self.__height_value = Entry(self.__mainwindow)

        self.__calculate_button = Button(self.__mainwindow,
                                         text="Calculate",
                                         background="green",
                                         command=self.calculate_BMI)

        self.__result_text = Label(self.__mainwindow, text="")
        self.__explanation_text = Label(self.__mainwindow, text="")

        self.__stop_button = Button(self.__mainwindow,
                                    text="Exit",
                                    background="red",
                                    command=self.stop)

        self.__weight_text.grid(row=1, column=0, sticky=E + W)
        self.__weight_value.grid(row=1, column=1, sticky=E + W)
        self.__height_text.grid(row=2, column=0, sticky=E + W)
        self.__height_value.grid(row=2, column=1, sticky=E + W)
        self.__calculate_button.grid(row=3, column=0, columnspan=2, sticky=E)
        self.__stop_button.grid(row=4, column=1, columnspan=2, sticky=E)
        self.__result_text.grid(row=5, column=0, columnspan=2, sticky=E)
        self.__explanation_text.grid(row=6, column=0, columnspan=2, sticky=E)

        self.__rikki = False
    def reset_fields(self):
        """ In error situations this method will zeroize the elements
            self.__result_text, self.__height_value, and self.__weight_value.
        """
        self.__result_text.configure(text="")
        self.__height_value.delete(0, END)
        self.__weight_value.delete(0, END)

    def get_values(self):
        try:
            weight = float(self.__weight_value.get())
            if weight < 0:
                self.__explanation_text.configure(text="Error: height and"
                                                       " weight must be "
                                                       "positive.")
                self.reset_fields()
                self.__rikki = True
        except (ValueError, AttributeError):
            weight = NAN
            self.__explanation_text.configure(text="Error: height and "
                                                   "weight must be numbers.")
            self.reset_fields()
            self.__rikki = True

        try:
            height = float(self.__height_value.get())
            if height < 0:
                self.__explanation_text.configure(text="Error: height and "
                                                       "weight must be "
                                                       "positive.")
                self.reset_fields()
                self.__rikki = True
        except (ValueError, AttributeError):
            height = NAN
            self.__explanation_text.configure(text="Error: height and "
                                                   "weight must be numbers.")
            self.reset_fields()
            self.__rikki = True

        return weight, height

    def aseta_tulosarvo(self):
        self.__result_text.configure(text=self.__BMI)

    def calculate_BMI(self):
        """ Section b) This method calculates the BMI of the user and
            displays it. First the method will get the values of
            height and weight from the GUI components
            self.__height_value and self.__weight_value.  Then the
            method will calculate the value of the BMI and show it in
            the element self.__result_text. 
            
            Section e) Last, the method will display a verbal
            description of the BMI in the element
            self.__explanation_text.
        """
        if not self.__rikki:
            (weight, height) = self.get_values()
            height_meters = height / 100.0
            self.__BMI = weight / (height_meters ** 2)
            self.__BMI = f"{self.__BMI:.2f}"
            self.__BMI = float(self.__BMI)
            self.aseta_tulosarvo()
        self.__rikki = False

        if 18.5 < self.__BMI < 25:
            self.__explanation_text.configure(text="Your weight is normal.")
        elif self.__BMI >= 25:
            self.__explanation_text.configure(text="You are overweight.")
        elif self.__BMI <= 18.5:
            self.__explanation_text.configure(text="You are underweight.")

    def stop(self):
        """ Ends the execution of the program.
        """
        self.__mainwindow.destroy()

    def start(self):
        """ Starts the mainloop. 
        """
        self.__mainwindow.mainloop()


def main():
    ui = Userinterface()
    ui.start()


main()
