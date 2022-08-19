import math
from tkinter import *


FONT = ("Arial", 18, "normal")
TITLE_COLOR = "#182042"
LABEL_COLOR = "#293462"
RESULT_COLOR = "red"
RESULT_FONT = ("Arial", 18, "bold")


def BMI_fun():
    if weight_input.get() == '' or height_input.get() == '':
        pass
    else:
        weight = float(weight_input.get())
        height = float(height_input.get())
        BMI = weight / height ** 2

        if BMI < 18.5:
            message = f"Your BMI is {math.ceil(BMI)}, you are Underweight."
        elif BMI < 25:
            message = f"Your BMI is {math.ceil(BMI)}, you are Normal Weight."
        elif BMI < 30:
            message = f"Your BMI is {math.ceil(BMI)}, you are slightly overweight."
        elif BMI < 35:
            message = f"Your BMI is {math.ceil(BMI)}, you are obese"
        else:
            message = f"Your BMI is {math.ceil(BMI)}, you are clinically obese"

        result_label.config(text=message)


window = Tk()
window.title("BMI CALCULATOR")
window.minsize(width=1100, height=450)
window.config(padx=20, pady=20)


#   CANVAS
canvas = Canvas(width=450, height=337)
create_photo = PhotoImage(file="chart.png")
canvas.create_image(225, 169, image=create_photo)
canvas.grid(column=1, rowspan=7)


#   TITLE LABEL
title_label = Label(text="BODY MASS INDEX", font=("Arial", 40, "bold"), fg=TITLE_COLOR)
title_label.config(padx=20, pady=20)
title_label.grid(column=0, row=0)


#   WEIGHT LABEL AND ENTRY
weight_label = Label(text="Enter Weight in Killograms", font=FONT, fg=LABEL_COLOR)
weight_label.grid(column=0, row=1)

weight_input = Entry(width=20, bd=5, font=20)
weight_input.focus()
weight_input.grid(column=0, row=2)


#   HEIGHT LABEL AND ENTRY
height_label = Label(text="Enter Hight in Meters", font=FONT, fg=LABEL_COLOR)
height_label.grid(column=0, row=3)

height_input = Entry(width=20, font=20, bd=5)
height_input.grid(column=0, row=4)


#   RESULT WITH MESSAGE
result_label = Label(text="", font=RESULT_FONT, fg=RESULT_COLOR, relief=RAISED)
result_label.config(padx=10, pady=10)
result_label.grid(column=0, row=5, padx=10, pady=10)



#   CALCULATOR BUTTON
calculate = Button(text="CALCULATE", command=BMI_fun, fg="white", bg="black")
calculate.grid(column=0, row=6)


window.mainloop()
