from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
TESTED_LANG = "French"
ANSWER_LANG = "English"

words_pair = {}

try:
    df = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    df = pd.read_csv("data/french_words.csv")
    to_learn = df.to_dict(orient='records')
else:
    to_learn = df.to_dict(orient='records')


# -----new card Generation-----
def generate_card():
    global words_pair, flip_timer
    window.after_cancel(flip_timer)
    words_pair = random.choice(to_learn)
    tested = words_pair[TESTED_LANG]
    canvas.itemconfig(card_title, text=TESTED_LANG, fill="black")
    canvas.itemconfig(card_word, text=tested, fill="black")
    canvas.itemconfig(card_img, image=front_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    global words_pair
    answer = words_pair[ANSWER_LANG]
    canvas.itemconfig(card_title, text=ANSWER_LANG, fill="white")
    canvas.itemconfig(card_word, text=answer, fill="white")
    canvas.itemconfig(card_img, image=back_img)


def known_word():
    to_learn.remove(words_pair)
    new_df = pd.DataFrame(to_learn)
    new_df.to_csv("data/words_to_learn.csv", index=False)
    generate_card()


# -----UI-----
window = Tk()
window.title("French-English Vocabulary")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

# Canvas
canvas = Canvas(width=800, height=526)
canvas.grid(column=0, row=0, columnspan=2)
front_img = PhotoImage(file="images/card_front.png")
back_img = PhotoImage(file="images/card_back.png")
card_img = canvas.create_image(400, 263, image=front_img)
card_title = canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="Word", font=("Arial", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)

# Buttons
cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=generate_card)
unknown_button.grid(column=0, row=1)
check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=known_word)
known_button.grid(column=1, row=1)

generate_card()

window.mainloop()
