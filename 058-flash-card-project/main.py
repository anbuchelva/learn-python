import tkinter as tk
import random as rand
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"
random_word = {}

# --------- Open file and store in dict --------------
try:
    data = pd.read_csv("data/words_to_learn.csv", encoding='latin-1')
except FileNotFoundError:
    data = pd.read_csv("data/french_words.csv")
except pd.errors.EmptyDataError:
    data = pd.read_csv("data/french_words.csv")
finally:
    to_learn = data.to_dict(orient="records")
    print(len(to_learn))
# ----------------------------------------------------


def next_card():
    global random_word
    global flip_timer
    window.after_cancel(flip_timer)
    random_word = rand.choice(to_learn)
    french_word = random_word["French"]
    # print(french_word)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_text, text=french_word, fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)


def is_known():
    # print(to_learn)
    to_learn.remove(random_word)
    next_card()
    print(len(to_learn))
    data = pd.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False, encoding='latin-1')


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    english_word = random_word["English"]
    # print(english_word)
    canvas.itemconfig(card_text, text=english_word, fill="white")
    canvas.itemconfig(card_background, image=card_back_img)


window = tk.Tk()
window.title("Learn French from Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

canvas = tk.Canvas(width=800, height=526, highlightthickness=0)
card_front_img = tk.PhotoImage(file="images/card_front.png")
card_back_img = tk.PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="Title",
                                font=("Ariel", 40, "italic"))
card_text = canvas.create_text(400, 263, text="word",
                               font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR)
canvas.grid(row=0, column=0, columnspan=2)

cross_image = tk.PhotoImage(file="images/wrong.png")
unknown_button = tk.Button(image=cross_image, highlightthickness=0,
                           command=next_card)
unknown_button.grid(row=1, column=0)

check_image = tk.PhotoImage(file="images/right.png")
known_button = tk.Button(image=check_image, highlightthickness=0,
                         command=is_known)
known_button.grid(row=1, column=1)

next_card()

window.mainloop()
