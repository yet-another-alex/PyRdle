from tkinter import *
from turtle import bgcolor
from pyrdle import *

# Constants
MIN_WIDTH = 2
MIN_HEIGHT = 1
FONT_SIZE = 64
C_GREY = '#2a2a2c'
C_YELLOW = '#ad952b'
C_GREEN = '#44813f'

# WORDS
wordlist = 'wordlist.txt'
words = []

# Tkinter initialization
root = Tk()
root.title('PyRdle')

# game instance
pyrdle_game = PyrdleGame('wordlist.txt')


def key_up(e):
    if e.char.isalpha() and not pyrdle_game.solved:
        if pyrdle_game.current_idx <= 5 and pyrdle_game.current_guess < 7:
            widget_name = f"{pyrdle_game.current_guess}_{pyrdle_game.current_idx}"
            current_box = root.nametowidget(widget_name)

            if len(pyrdle_game.current_try) < 5:
                pyrdle_game.current_try += e.char.upper()
            else:
                letters = list(pyrdle_game.current_try)
                letters[4] = e.char.upper()
                pyrdle_game.current_try = ''.join(letters)
            
            current_box['text'] = e.char.upper()

            # increment index
            if pyrdle_game.current_idx < 5:
                pyrdle_game.current_idx += 1


def key_backspace(e):
    if pyrdle_game.current_idx >= 1 and pyrdle_game.current_guess < 7 and not pyrdle_game.solved:

        widget_name = f"{pyrdle_game.current_guess}_{pyrdle_game.current_idx}"
        current_box = root.nametowidget(widget_name)

        current_box['text'] = ''
        pyrdle_game.current_try = pyrdle_game.current_try[:-1]
        if pyrdle_game.current_idx > 1:
            pyrdle_game.current_idx -= 1


def key_return(e):
    print(pyrdle_game.current_idx)
    print(pyrdle_game.is_valid())
    print(pyrdle_game.current_try)
    if pyrdle_game.current_idx == 5 and pyrdle_game.is_valid() and not pyrdle_game.solved:
        # evaluate current guess
        evaluate()

        # reset current try
        pyrdle_game.current_try = ''

        # increment counters for next guess
        pyrdle_game.current_guess += 1
        pyrdle_game.current_idx = 1
    elif not pyrdle_game.is_valid():
        label_bottom['text'] = 'Word not found in list!'


def evaluate():
    green_counter = 0
    for idx in range(1, 6):
        widget_name = f"{pyrdle_game.current_guess}_{idx}"
        current_box = root.nametowidget(widget_name)

        box_char = current_box['text']
        if box_char == pyrdle_game.current_word[idx-1]:
            current_box.configure(background=C_GREEN)
            green_counter += 1
        elif box_char in pyrdle_game.current_word:
            current_box.configure(background=C_YELLOW)

    # game is over and the player won
    if green_counter == 5:
        label_bottom['text'] = f"SOLVED! In {pyrdle_game.current_guess} tries!"
        pyrdle_game.solved = True

    # game is over but the player didn't win
    if green_counter != 5 and pyrdle_game.current_guess == 6:
        label_bottom['text'] = f"The word was {pyrdle_game.current_word}!"
        pyrdle_game.solved = True


def reset():
    for row_idx in range(1, 7):
        for col_idx in range(1, 6):
            widget_name = f"{row_idx}_{col_idx}"
            box = root.nametowidget(widget_name)
            box.configure(background=C_GREY)
            box['text'] = ''
    pyrdle_game.reset()
    pyrdle_game.pick_word()
    pyrdle_game.solved = False


"""
TKinter Definition of the GUI.
"""

label_title = Label(root, text='PyRdle', anchor=CENTER, font=(None, int(FONT_SIZE/2)))
label_title.grid(row=0, column=0, columnspan=5)

for row_idx in range(1, 7):
    for col_idx in range(1, 6):
        name = f"{row_idx}_{col_idx}"
        label = Label(root, width=MIN_WIDTH, height=MIN_HEIGHT, name=name, background=C_GREY, font=(None, FONT_SIZE), borderwidth=2, relief='solid')
        label.grid(row=row_idx, column=col_idx, sticky=NSEW)

label_bottom = Label(root, text='Start guessing!', anchor=W, font=(None, int(FONT_SIZE/4)))
label_bottom.grid(row=8, column=0, columnspan=4)

button_again = Button(root, text='AGAIN', anchor=CENTER, font=(None, int(FONT_SIZE/4)), command=reset)
button_again.grid(row=8, column=5)

# event handler
root.bind("<KeyRelease>", key_up)
root.bind("<BackSpace>", key_backspace)
root.bind("<Return>", key_return)

# pick a random word
pyrdle_game.pick_word()

# Tkinter main loop
root.mainloop()