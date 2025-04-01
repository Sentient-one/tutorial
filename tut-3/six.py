import tkinter as tk

def convert_to_uppercase():

    input_text = input_field.get()
    

    result = input_text.upper()

    result_var.set(result)

window = tk.Tk()
window.title("Uppercase Converter")
window.geometry("400x200")

result_var = tk.StringVar()

input_label = tk.Label(window, text="Enter text:")
input_label.pack(pady=(20, 5))

input_field = tk.Entry(window, width=40)
input_field.pack(pady=5)

convert_button = tk.Button(window, text="Convert to Uppercase", command=convert_to_uppercase)
convert_button.pack(pady=10)

result_label = tk.Label(window, text="Result:")
result_label.pack(pady=(10, 5))

result_display = tk.Label(window, textvariable=result_var, bg="lightgray", width=40, height=2)
result_display.pack(pady=5)


window.mainloop()