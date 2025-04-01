import tkinter as tk
from tkinter import messagebox
import random


secret_number = random.randint(1, 100)
attempts = 0

def check_guess():
    global attempts
    guess = entry.get()
    
    if not guess.isdigit():
        messagebox.showerror("Error", "Please enter a valid number!")
        return

    guess = int(guess)
    attempts += 1

    if guess < secret_number:
        result_label.config(text="Too small, try again!")
    elif guess > secret_number:
        result_label.config(text="Too large, try again!")
    else:
        messagebox.showinfo("Congratulations!", f"You guessed it in {attempts} attempts!")
        root.destroy() 


root = tk.Tk()
root.title("Guess the Number")

tk.Label(root, text="Guess a number between 1 and 100:").pack(pady=5)
entry = tk.Entry(root)
entry.pack(pady=5)

tk.Button(root, text="Submit Guess", command=check_guess).pack(pady=5)
result_label = tk.Label(root, text="")
result_label.pack(pady=5)

root.mainloop()
