import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        h = float(height_entry.get())
        b = float(bounce_entry.get())
        n = int(bounces_entry.get())
        
        if h <= 0 or b <= 0 or n < 0 or b >= 1:
            messagebox.showerror("Error", "Height and bounce must be positive, bounce < 1, bounces >= 0")
            return
            
        total = h
        current = h
        for _ in range(n):
            current *= b
            total += current * 2
            
        result.config(text=f"Distance: {total:.2f}")
        
    except ValueError:
        messagebox.showerror("Error", "Enter valid numbers")

# Window setup
root = tk.Tk()
root.title("Ball Distance")
root.geometry("200x200")

# Widgets
tk.Label(root, text="Height:").pack()
height_entry = tk.Entry(root)
height_entry.pack()

tk.Label(root, text="Bounce (0-1):").pack()
bounce_entry = tk.Entry(root)
bounce_entry.pack()

tk.Label(root, text="Bounces:").pack()
bounces_entry = tk.Entry(root)
bounces_entry.pack()

tk.Button(root, text="Calculate", command=calculate).pack(pady=10)
result = tk.Label(root, text="Distance: ")
result.pack()

root.mainloop()