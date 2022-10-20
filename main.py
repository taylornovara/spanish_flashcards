import tkinter

BACKGROUND_COLOR = "#B1DDC6"
FONT = "Ariel"

# GUI Setup
window = tkinter.Tk()
window.title("Spanish Flashcard")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Creates our flashcard
canvas = tkinter.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = tkinter.PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=card_front_img, )
canvas.create_text(400, 150, text="TITLE", font=(FONT, 40, "italic"), fill='black')
canvas.create_text(400, 263, text="word", font=(FONT, 60, "bold"), fill='black')
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
wrong_button_img = tkinter.PhotoImage(file="images/wrong.png")
wrong_button = tkinter.Button(image=wrong_button_img, border=0, highlightthickness=0, width=95, height=95)
wrong_button.grid(row=1, column=0, pady=50)

right_button_img = tkinter.PhotoImage(file="images/right.png")
right_button = tkinter.Button(image=right_button_img, border=0, highlightthickness=0, width=95, height=95)
right_button.grid(row=1, column=1, pady=50)

# Keeps program window open
window.mainloop()
