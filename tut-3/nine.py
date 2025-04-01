import tkinter as tk
import random

def new_game():
    global low, high, attempts, computer_guess
    low, high, attempts = 1, 100, 0
    computer_guess = random.randint(low, high)
    update_label()
    enable_buttons()

def update_label():
    guess_label.config(text=f"My guess: {computer_guess}")

def too_small():
    global low, computer_guess, attempts
    low = computer_guess + 1
    make_guess()

def too_large():
    global high, computer_guess, attempts
    high = computer_guess - 1
    make_guess()

def make_guess():
    global computer_guess, attempts
    attempts += 1
    if low > high:
        guess_label.config(text="Something went wrong!")
        disable_buttons()
    else:
        computer_guess = random.randint(low, high)
        update_label()

def correct():
    guess_label.config(text=f"I guessed it in {attempts} attempts! ")
    disable_buttons()

def disable_buttons():
    too_small_btn.config(state=tk.DISABLED)
    too_large_btn.config(state=tk.DISABLED)
    correct_btn.config(state=tk.DISABLED)

def enable_buttons():
    too_small_btn.config(state=tk.NORMAL)
    too_large_btn.config(state=tk.NORMAL)
    correct_btn.config(state=tk.NORMAL)


root = tk.Tk()
root.title("Computer Guessing Game")

guess_label = tk.Label(root, text="", font=("Arial", 14))
guess_label.pack(pady=10)

too_small_btn = tk.Button(root, text="Too Small", command=too_small)
too_large_btn = tk.Button(root, text="Too Large", command=too_large)
correct_btn = tk.Button(root, text="Correct", command=correct)
new_game_btn = tk.Button(root, text="New Game", command=new_game)

too_small_btn.pack(pady=5)
too_large_btn.pack(pady=5)
correct_btn.pack(pady=5)
new_game_btn.pack(pady=10)

new_game()
root.mainloop()
