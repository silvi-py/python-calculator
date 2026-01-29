"""
Simple Calculator - SILVESTAR CHURENSKI
"""
import tkinter as tk

# Create main window
window = tk.Tk()
window.title("Python Calculator - Silvestar Churenski")
window.geometry("350x500")
window.configure(bg="black")

# Variables
currentNumber = "0"
firstNumber = None
operator = None
waitingForSecondNumber = False

# Functions
def updateScreen():
    displayLabel.config(text=currentNumber)

def addNumber(number):
    global currentNumber, waitingForSecondNumber
    
    if currentNumber == "0" or currentNumber == "Error" or waitingForSecondNumber:
        currentNumber = str(number)
        waitingForSecondNumber = False
    else:
        if number == "." and "." in currentNumber:
            return
        currentNumber += str(number)
    
    updateScreen()

def addOperator(op):
    global firstNumber, operator, waitingForSecondNumber
    
    if operator is not None and not waitingForSecondNumber:
        calculate()
    
    firstNumber = float(currentNumber)
    operator = op
    waitingForSecondNumber = True

def calculate():
    global currentNumber, firstNumber, operator, waitingForSecondNumber
    
    if operator is None or firstNumber is None:
        return
    
    secondNumber = float(currentNumber)
    result = None
    
    if operator == "+":
        result = firstNumber + secondNumber
    elif operator == "-":
        result = firstNumber - secondNumber
    elif operator == "×":
        result = firstNumber * secondNumber
    elif operator == "÷":
        if secondNumber == 0:
            currentNumber = "Error"
            updateScreen()
            return
        result = firstNumber / secondNumber
    
    result = round(result, 8)
    
    if result == int(result):
        currentNumber = str(int(result))
    else:
        currentNumber = str(result)
    
    operator = None
    firstNumber = None
    waitingForSecondNumber = True
    updateScreen()

def clearScreen():
    global currentNumber, firstNumber, operator, waitingForSecondNumber
    currentNumber = "0"
    firstNumber = None
    operator = None
    waitingForSecondNumber = False
    updateScreen()

def backspace():
    global currentNumber
    
    if len(currentNumber) > 1 and currentNumber != "Error":
        currentNumber = currentNumber[:-1]
    else:
        currentNumber = "0"
    
    updateScreen()

# Display
displayLabel = tk.Label(
    window,
    text=currentNumber,
    font=("Arial", 36),
    bg="black",
    fg="white",
    width=15,
    height=2
)
displayLabel.pack(pady=20)

# Author name
authorLabel = tk.Label(
    window,
    text="SILVESTAR CHURENSKI - Python Calculator",
    font=("Arial", 10),
    bg="black",
    fg="white"
)
authorLabel.pack()

# Buttons frame
buttonsFrame = tk.Frame(window, bg="black")
buttonsFrame.pack(pady=20)

# Button colors
def getColor(text):
    if text in ["C", "⌫"]:
        return "#a6a6a6", "black"
    elif text in ["÷", "×", "-", "+", "="]:
        return "white", "black"
    else:
        return "#333333", "white"

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
            bgColor, fgColor = getColor(text)
            
            if text == "C":
                command = clearScreen
            elif text == "⌫":
                command = backspace
            elif text == "=":
                command = calculate
            elif text in ["÷", "×", "-", "+"]:
                command = lambda t=text: addOperator(t)
            else:
                command = lambda t=text: addNumber(t)
            
            if text == "0":
                button = tk.Button(
                    buttonsFrame,
                    text=text,
                    font=("Arial", 18),
                    bg=bgColor,
                    fg=fgColor,
                    command=command,
                    width=8,
                    height=2
                )
                button.grid(row=row, column=col, columnspan=2, padx=5, pady=5)
            else:
                button = tk.Button(
                    buttonsFrame,
                    text=text,
                    font=("Arial", 18),
                    bg=bgColor,
                    fg=fgColor,
                    command=command,
                    width=4,
                    height=2
                )
                button.grid(row=row, column=col, padx=5, pady=5)

# Run
window.mainloop()
