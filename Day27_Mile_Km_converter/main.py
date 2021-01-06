from tkinter import *


FONT = ("Arial", 16, "normal")


def miles_to_km():
    user_input = mile_input.get()
    km_result = round((float(user_input) * 1.60934))
    km_value.config(text=str(km_result))


def add_padding(item, pad_x=10, pad_y=10):
    item.config(padx=pad_x, pady=pad_y)


window = Tk()
window.title("Mile to Kilometers Converter")
window.minsize(width=300, height=150)
add_padding(window, pad_x=30, pad_y=30)

# Label
is_equal = Label(text="is equal to", font=FONT)
is_equal.grid(column=0, row=1)
miles = Label(text="Miles", font=FONT)
miles.grid(column=2, row=0)
km = Label(text="Km", font=FONT)
km.grid(column=2, row=1)
km_value = Label(text="0", font=FONT)
km_value.grid(column=1, row=1)


# Button
calculate = Button(text="Calculate", font=FONT, command=miles_to_km)
calculate.grid(column=1, row=2)


# Entry
mile_input = Entry(width=20, font=FONT)
mile_input.grid(column=1, row=0)


# Add paddings to all widgets
widgets = [is_equal, miles, km, km_value, calculate]
for widget in widgets:
    add_padding(widget)


window.mainloop()