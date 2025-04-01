import tkinter as tk


window = tk.Tk()
window.title("Temperature Converter")


fahrenheit_var = tk.StringVar(value="32.0")
celsius_var = tk.StringVar(value="0.0")


tk.Label(window, text="Fahrenheit").grid(row=0, column=0, padx=5, pady=5)
tk.Label(window, text="Celsius").grid(row=0, column=1, padx=5, pady=5)

fahrenheit_entry = tk.Entry(window, textvariable=fahrenheit_var)
fahrenheit_entry.grid(row=1, column=0, padx=5, pady=5)
celsius_entry = tk.Entry(window, textvariable=celsius_var)
celsius_entry.grid(row=1, column=1, padx=5, pady=5)

def fahrenheit_to_celsius():
    try:
        fahrenheit = float(fahrenheit_var.get())
        celsius = (fahrenheit - 32) * 5/9
        celsius_var.set(f"{celsius:.1f}")
    except ValueError:
        celsius_var.set("Error")

def celsius_to_fahrenheit():
    try:
        celsius = float(celsius_var.get())
        fahrenheit = celsius * 9/5 + 32
        fahrenheit_var.set(f"{fahrenheit:.1f}")
    except ValueError:
        fahrenheit_var.set("Error")

tk.Button(window, text=">>>>", command=fahrenheit_to_celsius).grid(row=2, column=0, padx=5, pady=5)
tk.Button(window, text="<<<<", command=celsius_to_fahrenheit).grid(row=2, column=1, padx=5, pady=5)
window.mainloop()