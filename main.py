import tkinter

import pandas
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
FONT = "Ariel"
word = {}
data = {}

try:
    # Opens spanish_words.csv, saves the dataframe to a dictionary, and organizes the dictionary to column-value.
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/spanish_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def new_word():
    """Generates a new Spanish word to display on the flashcard"""

    # Stores the random Spanish word in a global variable called word
    global word

    # Cancels the 3-second timer in flip_timer
    global flip_timer
    window.after_cancel(flip_timer)

    # Random word
    word = random.choice(to_learn)

    # Writes the title and word onto the canvas
    canvas.itemconfig(card_title, text="Spanish", fill="black")
    canvas.itemconfig(card_word, text=word["Spanish"], fill="black")

    # Resets the card to front image and font color
    canvas.itemconfig(card_image, image=card_front_img)

    # Turns the card over after 3 seconds
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    """Flips the card and shows the English translation to the current word"""

    # Changes the title, English translation, font color, and background image of the current card.
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=word["English"], fill="white")
    canvas.itemconfig(card_image, image=card_back_img)


def is_known():
    """Removes the word from the csv file so that it won't be shown again and calls new_word()"""

    to_learn.remove(word)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    new_word()


# GUI Setup
window = tkinter.Tk()
window.title("Spanish Flashcards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Flips the card after 3 seconds
flip_timer = window.after(3000, func=flip_card)

# Creates our icon.
icon = tkinter.PhotoImage(file="images/spanish.png")
window.iconphoto(False, icon)

# Creates our flashcard
canvas = tkinter.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = tkinter.PhotoImage(file="images/card_front.png")
card_image = canvas.create_image(400, 263, image=card_front_img)
card_back_img = tkinter.PhotoImage(file="images/card_back.png")
card_title = canvas.create_text(400, 150, text="", font=(FONT, 40, "italic"), fill='black')
card_word = canvas.create_text(400, 263, text=f"", font=(FONT, 40, "bold"), fill='black')
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
wrong_button_img = tkinter.PhotoImage(file="images/wrong.png")
wrong_button = tkinter.Button(image=wrong_button_img, border=0, highlightthickness=0, width=95, height=95,
                              command=new_word)
wrong_button.grid(row=1, column=0, pady=50)

right_button_img = tkinter.PhotoImage(file="images/right.png")
right_button = tkinter.Button(image=right_button_img, border=0, highlightthickness=0, width=95, height=95,
                              command=is_known)
right_button.grid(row=1, column=1, pady=50)

# Calls new_word() so that a Spanish word is displayed
new_word()

# Keeps program window open
window.mainloop()
