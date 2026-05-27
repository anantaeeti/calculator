import tkinter as tk
import math

# Create main window
root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("850x600")

# Theme state
dark_mode = False

# Colors
LIGHT_BG = "#f5f5f5"
LIGHT_BTN = "#ffffff"
LIGHT_TEXT = "#000000"

DARK_BG = "#1e1e1e"
DARK_BTN = "#2d2d2d"
DARK_TEXT = "#ffffff"

ACCENT = "#ffb347"   # orange-yellow
ACCENT2 = "#ffcc70"

# Entry field
entry = tk.Entry(
    root,
    width=25,
    font=("Arial", 24),
    borderwidth=5,
    relief="ridge",
    justify="right",
    bg="white",
    fg="black"
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

# Function to delete last character
def backspace():
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current[:-1])

# Function to calculate result
def calculate():
    try:
        expression = entry.get()

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

# Toggle dark mode
def toggle_dark_mode():
    global dark_mode
    dark_mode = not dark_mode

    if dark_mode:
        root.configure(bg=DARK_BG)
        frame.configure(bg=DARK_BG)

        entry.configure(
            bg=DARK_BTN,
            fg=DARK_TEXT,
            insertbackground="white"
        )

        for button in all_buttons:
            button.configure(
                bg=DARK_BTN,
                fg=DARK_TEXT,
                activebackground=ACCENT,
                activeforeground="black"
            )

    else:
        root.configure(bg=LIGHT_BG)
        frame.configure(bg=LIGHT_BG)

        entry.configure(
            bg="white",
            fg=LIGHT_TEXT,
            insertbackground="black"
        )

        for button in all_buttons:
            button.configure(
                bg=LIGHT_BTN,
                fg=LIGHT_TEXT,
                activebackground=ACCENT2,
                activeforeground="black"
            )

# Main background
root.configure(bg=LIGHT_BG)

# Button frame
frame = tk.Frame(root, bg=LIGHT_BG)
frame.pack(expand=True, fill='both')

# Button layout
buttons = [
    ['7', '8', '9', '/', '%'],
    ['4', '5', '6', '*', '//'],
    ['1', '2', '3', '-', '**'],
    ['0', '.', '(', ')', '+'],

    ['sin(', 'cos(', 'tan(', 'sqrt(', 'pi'],
    ['asin(', 'acos(', 'atan(', 'log(', 'e'],

    ['log10(', '⌫', 'C', '=', '🌙']
]

all_buttons = []

# Create buttons
for row in buttons:
    row_frame = tk.Frame(frame, bg=LIGHT_BG)
    row_frame.pack(expand=True, fill='both')

    for btn in row:

        # Empty spaces
        if btn == '':
            tk.Label(
                row_frame,
                text='',
                width=5,
                bg=LIGHT_BG
            ).pack(side='left', expand=True, fill='both')
            continue

        # Special buttons
        if btn == "=":
            action = calculate

        elif btn == "C":
            action = clear

        elif btn == "⌫":
            action = backspace

        elif btn == "🌙":
            action = toggle_dark_mode

        else:
            action = lambda x=btn: click(x)

        # Accent colors for important buttons
        if btn in ['=', 'C', '⌫', '🌙']:
            btn_bg = ACCENT
        else:
            btn_bg = LIGHT_BTN

        button = tk.Button(
            row_frame,
            text=btn,
            font=("Arial", 16, "bold"),
            command=action,
            height=2,
            width=5,
            bg=btn_bg,
            fg=LIGHT_TEXT,
            activebackground=ACCENT2,
            relief="flat",
            borderwidth=0
        )

        button.pack(side='left', expand=True, fill='both', padx=3, pady=3)

        all_buttons.append(button)

# Run app
root.mainloop()