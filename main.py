import random
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"
c_card = {}
try:
    data = pd.read_csv('data/updated_data.csv')
    dict = data.to_dict(orient='records')
except FileNotFoundError:
    data = pd.read_csv('data/french_words.csv')
    dict = data.to_dict(orient='records')

def next_card():
    global c_card, flip_timer
    window.after_cancel(flip_timer) #canceling the timer each time its started
    c_card = random.choice(dict)
    random_fword = c_card['French']
    canvas.itemconfig(card_title, text='French', fill='black')
    canvas.itemconfig(card_word, text=random_fword, fill='black')
    canvas.itemconfig(card_bg, image=front_image)
    flip_timer = window.after(3000, func=flip_card) #starting the timer again for 3 seconds

def flip_card():
    global c_card
    canvas.itemconfig(card_title, text="English", fill='white')
    canvas.itemconfig(card_word, text=c_card['English'], fill='white')
    canvas.itemconfig(card_bg, image=back_image)

def update_file():
    global c_card
    dict.remove(c_card)
    mod_data = pd.DataFrame(dict)
    mod_data.to_csv("data/updated_data.csv", index=False)
    next_card()


#from tkinter import *
from tkinter import Tk, Canvas, PhotoImage, Button
window = Tk()
window.title("Flash Card Application")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, background=BACKGROUND_COLOR, highlightthickness=0)
front_image = PhotoImage(file="images/card_front.png")
back_image = PhotoImage(file="images/card_back.png")

card_bg = canvas.create_image(400, 263, image=front_image)
card_title = canvas.create_text(400, 150, text="Title", font=('Ariel', 40, 'italic'))
card_word = canvas.create_text(400, 300, text="Word", font=('Ariel', 45, 'bold'))
canvas.grid(row=0, column=0, columnspan=2)

wrong_pic = PhotoImage(file='images/wrong.png')
wrong_btn = Button(image=wrong_pic, highlightthickness=0, border=0, command=next_card)
wrong_btn.grid(row=1, column=0)

right_pic = PhotoImage(file='images/right.png')
right_btn = Button(image=right_pic, highlightthickness=0, border=0, command=update_file)
right_btn.grid(row=1, column=1)

next_card()
window.mainloop()