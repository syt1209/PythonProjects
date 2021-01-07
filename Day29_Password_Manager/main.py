from tkinter import *
from tkinter import messagebox
import random
import pyperclip

FONT = ("Courier", 10, "bold")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generator():
    password_entry.delete(0, END)

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    letters_selected = random.sample(letters, nr_letters)
    numbers_selected = random.sample(numbers, nr_numbers)
    symbols_selected = random.sample(symbols, nr_symbols)

    password_list = letters_selected + symbols_selected + numbers_selected

    # randomize
    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(END, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    user_id = user_ID_entry.get()
    password = password_entry.get()

    # Confirm with user using popups
    if len(website) == 0:
        messagebox.showwarning(title="Warning", message="Website missing...")
    elif len(password) == 0:
        messagebox.showwarning(title="Warning", message="Password missing...")
    else:
        is_ok = messagebox.askokcancel(title="Confirmation", message=f'These are the information you have entered.\n '
                                                                     f'Website: {website}\n Email: {user_id}\n '
                                                                     f'Password: {password}')
        if is_ok:
            with open("password.txt", "a") as f:
                f.write(f"{website} | {user_id} | {password}\n")

            website_entry.delete(0, END)
            user_ID_entry.delete(0, END)
            user_ID_entry.insert(0, "syt1209@gmail.com")
            password_entry.delete(0, END)
            website_entry.focus()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Canvas
canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website", font=FONT)
website_label.grid(column=0, row=1)

user_ID_label = Label(text="Email/Username", font=FONT)
user_ID_label.grid(column=0, row=2)

password_label = Label(text="Password", font=FONT)
password_label.grid(column=0, row=3)

# Buttons
generate_button = Button(text="Generate", font=FONT, command=generator)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", font=FONT, width=35, command=save)
add_button.grid(column=1, row=4, columnspan=2)

# Entries
website_entry = Entry(width=35, font=FONT)
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=2)

user_ID_entry = Entry(width=35, font=FONT)
user_ID_entry.insert(0, "syt1209@gmail.com")
user_ID_entry.grid(column=1, row=2, columnspan=2)

password_entry = Entry(width=25, font=FONT)
password_entry.grid(column=1, row=3)

window.mainloop()
