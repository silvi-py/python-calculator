"""
Simple Calculator - SILVESTAR CHURENSKI
"""

import tkinter as tk

# Create main window
window = tk.Tk()
window.title("Python Calculator - Silvestar Churenski")
window.geometry("350x500")
window.configure(bg="black")

# Display text
display_text = "0"

# Functions
def add_number(number):
    global display_text
    if display_text == "0" or display_text == "Error":
        display_text = str(number)
    else:
        display_text += str(number)
    display_label.config(text=display_text)

def add_operation(op):
    global display_text
    display_text += op
    display_label.config(text=display_text)

def calculate():
    global display_text
    try:
        expression = display_text.replace('÷', '/').replace('×', '*')
        result = eval(expression)
        display_text = str(result)
    except:
        display_text = "Error"
    display_label.config(text=display_text)

def clear_screen():
    global display_text
    display_text = "0"
    display_label.config(text=display_text)

def backspace():
    global display_text
    if len(display_text) > 1:
        display_text = display_text[:-1]
    else:
        display_text = "0"
    display_label.config(text=display_text)

# Display
display_label = tk.Label(
    window,
    text=display_text,
    font=("Arial", 36),
    bg="black",
    fg="white",
    width=15,
    height=2
)
display_label.pack(pady=20)

# Author name
author_label = tk.Label(
    window,
    text="SILVESTAR CHURENSKI - Python Calculator",
    font=("Arial", 10),
    bg="black",
    fg="white"
)
author_label.pack()

# Buttons frame
buttons_frame = tk.Frame(window, bg="black")
buttons_frame.pack(pady=20)

# Button colors
def get_color(text):
    if text in ["C", "⌫"]:
        return "#a6a6a6", "black"  # Light gray
    elif text in ["÷", "×", "-", "+", "="]:
        return "white", "black"     # White
    else:
        return "#333333", "white"   # Dark gray

# Buttons
buttons = [
    ["C", "⌫", "÷", "×"],
    ["7", "8", "9", "-"],
    ["4", "5", "6", "+"],
    ["1", "2", "3", "="],
    ["0", ".", "", ""]
]

# Create buttons
for row in range(5):
    for col in range(4):
        text = buttons[row][col]
        if text:
            bg_color, fg_color = get_color(text)
            
            # Commands
            if text == "C":
                command = clear_screen
            elif text == "⌫":
                command = backspace
            elif text == "=":
                command = calculate
            elif text in ["÷", "×", "-", "+"]:
                command = lambda t=text: add_operation(t)
            else:
                command = lambda t=text: add_number(t)
            
            # Create button
            if text == "0":
                button = tk.Button(
                    buttons_frame,
                    text=text,
                    font=("Arial", 18),
                    bg=bg_color,
                    fg=fg_color,
                    command=command,
                    width=8,
                    height=2
                )
                button.grid(row=row, column=col, columnspan=2, padx=5, pady=5)
            else:
                button = tk.Button(
                    buttons_frame,
                    text=text,
                    font=("Arial", 18),
                    bg=bg_color,
                    fg=fg_color,
                    command=command,
                    width=4,
                    height=2
                )
                button.grid(row=row, column=col, padx=5, pady=5)

# Run
window.mainloop()
