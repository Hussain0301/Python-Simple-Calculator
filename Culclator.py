import tkinter as tk
from tkinter import ttk
from math import *

# Initialize the main window
root = tk.Tk()
root.title("Advanced Graphical Calculator")
root.geometry("500x600")  # Set a fixed window size
root.configure(bg='#282828')  # Set background color to dark grey

# Define a modern style
style = ttk.Style()
style.configure("TButton",
                font=("Helvetica", 15),
                padding=10,
                borderwidth=0)
style.configure("TEntry",
                font=("Helvetica", 18),
                padding=5)
style.map("TButton",
          foreground=[('pressed', 'white'), ('active', 'black')],
          background=[('pressed', '#4CAF50'), ('active', '#D3D3D3')])

# Entry widget for input
entry = ttk.Entry(root, font=("Helvetica", 18), justify="right")
entry.grid(row=0, column=0, columnspan=5, padx=10, pady=20, sticky="nsew")

def button_click(value):
    """Handle button click."""
    current = entry.get()
    
    # Prevent multiple operators in a row
    if value in '+-×÷' and (current == "" or current[-1] in '+-×÷'):
        return
    
    # Update the entry field
    entry.insert(tk.END, str(value))

def button_clear():
    """Clear the entry widget."""
    entry.delete(0, tk.END)

def button_delete():
    """Delete the last character in the entry widget."""
    current = entry.get()
    entry.delete(len(current)-1, tk.END)

def button_equal():
    """Calculate the result."""
    try:
        current = entry.get()
        
        # Replace symbols for eval
        expression = current.replace('÷', '/').replace('×', '*').replace('√', 'sqrt')
        
        # Evaluate the expression
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Define button layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('÷', 1, 3), ('sin', 1, 4),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('×', 2, 3), ('cos', 2, 4),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3), ('tan', 3, 4),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('√', 4, 3), ('log', 4, 4),
    ('(', 5, 0), (')', 5, 1), ('Delete', 5, 2), ('Clear', 5, 3), ('=', 5, 4)
]

# Create buttons dynamically
for button in buttons:
    text = button[0]
    row = button[1]
    col = button[2]
    colspan = button[3] if len(button) > 3 else 1  # Handle colspan for equals button
    action = lambda x=text: button_click(x)
    
    if text == 'Clear':
        action = button_clear
    elif text == '=':
        action = button_equal
    elif text == 'Delete':
        action = button_delete
    
    ttk.Button(root, text=text, command=action).grid(row=row, column=col, columnspan=colspan, sticky="nsew", padx=5, pady=5)

# Adjust row and column weights for responsiveness
for i in range(6):
    root.grid_rowconfigure(i, weight=1)
for j in range(5):
    root.grid_columnconfigure(j, weight=1)

# Start the GUI event loop
root.mainloop()
