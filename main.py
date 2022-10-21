import tkinter
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
FONT = "Ariel"


def new_word():
    """Generates a new Spanish word to display on the flashcard"""

    # Random number
    random_number = random.randint(0, 99)

    df = pd.read_csv("data/spanish_words.csv")
    data = df.to_dict(orient="records")
    word = data[random_number]["Spanish"]
    canvas.itemconfig(card_title, text="Spanish")
    canvas.itemconfig(card_word, text=word)


# GUI Setup
window = tkinter.Tk()
window.title("Spanish Flashcards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Creates our icon.
icon = tkinter.PhotoImage(file="images/spanish.png")
window.iconphoto(False, icon)

# Creates our flashcard
canvas = tkinter.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = tkinter.PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=card_front_img, )
card_title = canvas.create_text(400, 150, text="Spanish Flashcards", font=(FONT, 40, "italic"), fill='black')
card_word = canvas.create_text(400, 263, text=f"Click the Green Check to Begin", font=(FONT, 40, "bold"), fill='black')
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
wrong_button_img = tkinter.PhotoImage(file="images/wrong.png")
wrong_button = tkinter.Button(image=wrong_button_img, border=0, highlightthickness=0, width=95, height=95,
                              command=new_word)
wrong_button.grid(row=1, column=0, pady=50)

right_button_img = tkinter.PhotoImage(file="images/right.png")
right_button = tkinter.Button(image=right_button_img, border=0, highlightthickness=0, width=95, height=95,
                              command=new_word)
right_button.grid(row=1, column=1, pady=50)

# Keeps program window open
window.mainloop()
