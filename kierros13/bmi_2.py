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

    def reset_fields(self):
        self.__result_text.configure(text="")
        self.__height_value.delete(0, END)
        self.__weight_value.delete(0, END)

    def calculate_BMI(self):
        try:
            weight = float(self.__weight_value.get())
            height = float(self.__height_value.get())
            if weight < 0 or height < 0:
                self.__explanation_text.configure(text="Error: height and"
                                                       " weight must be "
                                                       "positive.")
                self.reset_fields()
                return
        except (ValueError, AttributeError):
            self.__explanation_text.configure(text="Error: height and "
                                                   "weight must be numbers.")
            self.reset_fields()
            return

        height_meters = height / 100.0
        self.__BMI = weight / (height_meters ** 2)
        self.__BMI = float(f"{self.__BMI:.2f}")
        self.__result_text.configure(text=self.__BMI)

        if 18.5 < self.__BMI < 25:
            self.__explanation_text.configure(text="Your weight is normal.")
        elif self.__BMI >= 25:
            self.__explanation_text.configure(text="You are overweight.")
        elif self.__BMI <= 18.5:
            self.__explanation_text.configure(text="You are underweight.")

    def stop(self):
        self.__mainwindow.destroy()

    def start(self):
        self.__mainwindow.mainloop()

def main():
    ui = Userinterface()
    ui.start()


main()
