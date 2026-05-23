import tkinter as tk

# Create main window
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")

# Entry field
entry = tk.Entry(root, width=20, font=("Arial", 24), borderwidth=5, relief="ridge")
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
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Button frame
frame = tk.Frame(root)
frame.pack()

# Button layout
buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+']
]

# Create buttons
for row in buttons:
    row_frame = tk.Frame(frame)
    row_frame.pack(expand=True, fill='both')

    for btn in row:
        action = lambda x=btn: calculate() if x == '=' else click(x)

        tk.Button(
            row_frame,
            text=btn,
            font=("Arial", 18),
            command=action,
            height=2,
            width=5
        ).pack(side='left', expand=True, fill='both')

# Clear button
tk.Button(
    root,
    text="Clear",
    font=("Arial", 18),
    command=clear
).pack(fill='both', padx=10, pady=10)

# Run app
root.mainloop()