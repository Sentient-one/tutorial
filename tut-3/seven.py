import tkinter as tk
from tkinter import messagebox
import math

def compute_sqrt():
    try:
        num = int(entry.get()) 
        if num < 0:
            raise ValueError("Cannot compute square root of a negative number.")
        sqrt_result = math.sqrt(num)
        result_label.config(text=f"Square Root: {sqrt_result:.2f}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid non-negative integer.")


root = tk.Tk()
root.title("Square Root Calculator")

tk.Label(root, text="Enter an integer:").grid(row=0, column=0, padx=10, pady=10)
entry = tk.Entry(root)
entry.grid(row=0, column=1, padx=10, pady=10)

compute_btn = tk.Button(root, text="Compute √", command=compute_sqrt)
compute_btn.grid(row=1, column=0, columnspan=2, pady=10)
result_label = tk.Label(root, text="Square Root: ")
result_label.grid(row=2, column=0, columnspan=2, pady=10)
root.mainloop()
