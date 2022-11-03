import tkinter
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
FONT = "Ariel"

# Opens spanish_words.csv, saves the dataframe to a dictionary, and organizes the dictionary to column-value.
df = pd.read_csv("data/spanish_words.csv")
data = df.to_dict(orient="records")

word = {}


def new_word():
    """Generates a new Spanish word to display on the flashcard"""

    # Random number.
    random_number = random.randint(0, 99)

    # Stores the random Spanish word in a global variable called word
    global word
    word = data[random_number]

    # Cancels the 3-second timer in flip_timer
    global flip_timer
    window.after_cancel(flip_timer)

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
                              command=new_word)
right_button.grid(row=1, column=1, pady=50)

# Calls new_word() so that a Spanish word is displayed
new_word()

# Keeps program window open
window.mainloop()
