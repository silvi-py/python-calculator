import tkinter as tk
from tkinter import font

# Create main window
window = tk.Tk()
window.title("Modern Calculator - SILVESTAR CHURENSKI")
window.geometry("400x600")
window.configure(bg="#1a1a1a")

# Fonts
large_font = font.Font(family="Arial", size=24, weight="bold")
normal_font = font.Font(family="Arial", size=18)
small_font = font.Font(family="Arial", size=12)

# Screen
screen_frame = tk.Frame(window, bg="#1a1a1a", height=150)
screen_frame.pack(fill="both", padx=20, pady=(20, 10))

# Author name
author_label = tk.Label(
    screen_frame,
    text="SILVESTAR CHURENSKI",
    font=small_font,
    fg="#ffffff",
    bg="#1a1a1a"
)
author_label.pack(anchor="ne")

# Result display
result_label = tk.Label(
    screen_frame,
    text="0",
    font=large_font,
    fg="#ffffff",
    bg="#1a1a1a",
    anchor="e"
)
result_label.pack(fill="both", expand=True)

# Variables
current_number = "0"

# Functions
def number_click(number):
    global current_number
    if current_number == "0":
        current_number = str(number)
    else:
        current_number += str(number)
    result_label.config(text=current_number)

def clear():
    global current_number
    current_number = "0"
    result_label.config(text="0")

def calculate():
    global current_number
    try:
        result = eval(current_number)
        current_number = str(result)
        result_label.config(text=current_number)
    except:
        current_number = "Error"
        result_label.config(text="Error")

# Buttons
button_frame = tk.Frame(window, bg="#1a1a1a")
button_frame.pack(fill="both", expand=True, padx=20, pady=10)

buttons = [
    ("C", 0, 0, clear), ("7", 1, 0, lambda: number_click(7)), ("4", 2, 0, lambda: number_click(4)), ("1", 3, 0, lambda: number_click(1)),
    ("⌫", 0, 1, lambda: number_click("")), ("8", 1, 1, lambda: number_click(8)), ("5", 2, 1, lambda: number_click(5)), ("2", 3, 1, lambda: number_click(2)),
    ("÷", 0, 2, lambda: number_click("/")), ("9", 1, 2, lambda: number_click(9)), ("6", 2, 2, lambda: number_click(6)), ("3", 3, 2, lambda: number_click(3)),
    ("×", 0, 3, lambda: number_click("*")), ("-", 1, 3, lambda: number_click("-")), ("+", 2, 3, lambda: number_click("+")), ("=", 3, 3, calculate),
    ("0", 4, 0, lambda: number_click(0)), (".", 4, 1, lambda: number_click(".")),
]

for text, row, col, command in buttons:
    if text in ["C", "⌫"]:
        color = "#a6a6a6"
    elif text in ["÷", "×", "-", "+", "="]:
        color = "#ff9500"
    else:
        color = "#333333"
    
    btn = tk.Button(
        button_frame,
        text=text,
        font=normal_font,
        bg=color,
        fg="#ffffff" if color != "#a6a6a6" else "#000000",
        command=command
    )
    btn.grid(row=row, column=col, sticky="nsew", padx=5, pady=5, ipadx=10, ipady=20)

# Configure grid
for i in range(5):
    button_frame.grid_rowconfigure(i, weight=1)
for i in range(4):
    button_frame.grid_columnconfigure(i, weight=1)

# Run
window.mainloop()
