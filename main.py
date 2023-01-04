import tkinter
from tkinter import Button

BLACK = '#000000'
window = tkinter.Tk()
window.title("Vidya Calculator")
window.minsize(width=180, height=200)

output_label = tkinter.Label(font=("Italic", 24, "bold"))
output_label.grid(row=0, columnspan=3)
combined_arguments = ''


def combine_arguments(*args):
    for arg in args:
        global combined_arguments
        combined_arguments += arg
    button_clicked()


def button_clicked():
    output_label.config(text=combined_arguments)


def reset():
    output_label.config(text="")
    global combined_arguments
    combined_arguments = ""


def output():
    global combined_arguments
    actual_output = round(eval(combined_arguments), 3)
    combined_arguments = str(actual_output)
    output_label.config(text=actual_output)


number8 = Button(text="8", command=lambda: combine_arguments("8"), width=8, height=3)
number8.grid(row=1, column=0)

number9 = Button(text="9", command=lambda: combine_arguments("9"), width=8, height=3)
number9.grid(row=1, column=1)

clear_all = Button(text="AC", command=lambda: reset(), width=8, height=3)
clear_all.grid(row=1, column=2)

division = Button(text="÷", command=lambda: combine_arguments("/"), width=8, height=3)
division.grid(row=1, column=3)

number5 = Button(text="5", command=lambda: combine_arguments("5"), width=8, height=3)
number5.grid(row=2, column=0)

number6 = Button(text="6", command=lambda: combine_arguments("6"), width=8, height=3)
number6.grid(row=2, column=1)

number7 = Button(text="7", command=lambda: combine_arguments("7"), width=8, height=3)
number7.grid(row=2, column=2)

multiplication = Button(text="×", command=lambda: combine_arguments("*"), width=8, height=3)
multiplication.grid(row=2, column=3)

number2 = Button(text="2", command=lambda: combine_arguments("2"), width=8, height=3)
number2.grid(row=3, column=0)

number3 = Button(text="3", command=lambda: combine_arguments("3"), width=8, height=3)
number3.grid(row=3, column=1)

number4 = Button(text="4", command=lambda: combine_arguments("4"), width=8, height=3)
number4.grid(row=3, column=2)

subtraction = Button(text="-", command=lambda: combine_arguments("-"), width=8, height=3)
subtraction.grid(row=3, column=3)

number1 = Button(text="1", command=lambda: combine_arguments("1"), width=8, height=3)
number1.grid(row=4, column=0)

number0 = Button(text="0", command=lambda: combine_arguments("0"), width=8, height=3)
number0.grid(row=4, column=1)

equal_to = Button(text="=", command=output, width=8, height=3)
equal_to.grid(row=4, column=2)

addition = Button(text="+", command=lambda: combine_arguments("+"), width=8, height=3)
addition.grid(row=4, column=3)

button_clicked()

window.mainloop()
