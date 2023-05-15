from tkinter import *

window = Tk()
window.title("Poggers")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)


def button_clicked():
    my_label["text"] = input_field.get()


# Label
my_label = Label(text="Label", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)

# Button
button = Button(text="click me", command=button_clicked)
button.grid(column=1, row=1)

# new_Button
new_button = Button(text="new click me", command=button_clicked)
new_button.grid(column=2, row=0)


# Entry
input_field = Entry(width=10)
input_field.grid(column=3, row=2)



window.mainloop()
