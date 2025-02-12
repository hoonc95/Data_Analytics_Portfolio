import tkinter as tk
from tkinter import ttk

def convert():
    try:
        mile_input = float(entry.get())
        conversion_type = conversion_var.get()

        if conversion_type == 'mi to km':
            km_output = mile_input * 1.60934
            output_string.set(f'{km_output:.2f} km')
        elif conversion_type == 'km to mi':
            mile_output = mile_input / 1.60934
            output_string.set(f'{mile_output:.2f} mi')
    except ValueError:
        output_string.set("Invalid input")

# window
window = tk.Tk()
window.title('Distance Converter')
window.geometry('400x200')

# title
title_label = ttk.Label(
    master=window,
    text='Distance Converter',
    font=('Arial', 20, 'bold'))
title_label.pack(pady=20)

# conversion type selector
conversion_var = tk.StringVar(value='mi to km')
conversion_combobox = ttk.Combobox(
    master=window,
    textvariable=conversion_var,
    values=['mi to km', 'km to mi'],
    state='readonly')
conversion_combobox.pack(pady=5)

# input field
input_frame = ttk.Frame(master=window)
entry = ttk.Entry(
    master=input_frame,
    textvariable=tk.DoubleVar())
button = ttk.Button(
    master=input_frame,
    text='Convert',
    command=convert)
entry.pack(side='left', padx=10)
button.pack(side='left')
input_frame.pack(pady=5)

# output
output_string = tk.StringVar()
output_label = ttk.Label(
    master=window,
    text='Output',
    font=('Arial', 20),
    textvariable=output_string)
output_label.pack(pady=10)

# Enter key binding
window.bind('<Return>', lambda event: convert())

# run
window.mainloop()
