from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)


def calculate():
    miles = int(input_field.get())
    km = round(1.609344 * miles, 2)
    final.config(text=km)


# Label
my_label = Label(text="is equal to", font=("Arial", 12))
my_label.grid(column=0, row=1)

# Entry
input_field = Entry(width=10)
input_field.grid(column=1, row=0)

# Label
miles_label = Label(text="Miles", font=("Arial", 12))
miles_label.grid(column=2, row=0)

# Label
final = Label(text="0", font=("Arial", 12))
final.grid(column=1, row=1)

# Label
km_label = Label(text="Km", font=("Arial", 12))
km_label.grid(column=2, row=1)

# Button
button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)


window.mainloop()
