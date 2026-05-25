import tkinter as tk
import math

# Create main window
root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("850x600")

# Entry field
entry = tk.Entry(
    root,
    width=25,
    font=("Arial", 24),
    borderwidth=5,
    relief="ridge",
    justify="right"
)
entry.pack(pady=20)

# Function to add text
def click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(value))

# Function to clear entry
def clear():
    entry.delete(0, tk.END)

# Function to calculate result
def calculate():
    try:
        expression = entry.get()

        # Safe evaluation
        result = eval(
            expression,
            {"__builtins__": None},
            {
                "sqrt": math.sqrt,

                # Trigonometric functions
                "sin": math.sin,
                "cos": math.cos,
                "tan": math.tan,

                # Inverse trigonometric functions
                "asin": math.asin,
                "acos": math.acos,
                "atan": math.atan,

                # Logarithmic functions
                "log": math.log,
                "log10": math.log10,

                # Constants
                "pi": math.pi,
                "e": math.e
            }
        )

        entry.delete(0, tk.END)
        entry.insert(0, result)

    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Button frame
frame = tk.Frame(root)
frame.pack(expand=True, fill='both')

# Button layout
buttons = [
    ['7', '8', '9', '/', '%'],
    ['4', '5', '6', '*', '//'],
    ['1', '2', '3', '-', '**'],
    ['0', '.', '(', ')', '+'],

    ['sin(', 'cos(', 'tan(', 'sqrt(', 'pi'],
    ['asin(', 'acos(', 'atan(', 'log(', 'e'],

    ['log10(', 'C', '=']
]

# Create buttons
for row in buttons:
    row_frame = tk.Frame(frame)
    row_frame.pack(expand=True, fill='both')

    for btn in row:

        # Empty spaces
        if btn == '':
            tk.Label(
                row_frame,
                text='',
                width=5
            ).pack(side='left', expand=True, fill='both')
            continue

        # Special buttons
        if btn == "=":
            action = calculate

        elif btn == "C":
            action = clear

        else:
            action = lambda x=btn: click(x)

        tk.Button(
            row_frame,
            text=btn,
            font=("Arial", 16),
            command=action,
            height=2,
            width=5
        ).pack(side='left', expand=True, fill='both')

# Run app
root.mainloop()