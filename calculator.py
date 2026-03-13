import tkinter as tk

# Function to update expression in the entry box
def press(num):
    entry_text.set(entry_text.get() + str(num))

# Function to evaluate final expression
def equalpress():
    try:
        result = str(eval(entry_text.get()))
        entry_text.set(result)
    except Exception as e:
        entry_text.set("Error")

# Function to clear the entry box
def clear():
    entry_text.set("")

# Main GUI window
root = tk.Tk()
root.title("🧮 Simple Calculator")
root.geometry("300x500")
root.resizable(False, False)
root.configure(bg="#e6f2ff")

entry_text = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_text, font=('Arial', 20), bd=10, insertwidth=2, width=14, borderwidth=4, justify='right')
entry.grid(row=0, column=0, columnspan=4, pady=10)

# Buttons layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
    ('C', 5, 0)
]

# Create and place buttons
for (text, row, col) in buttons:
    if text == '=':
        btn = tk.Button(root, text=text, padx=20, pady=20, bg="lightgreen", font=('Arial', 12), command=equalpress)
    elif text == 'C':
        btn = tk.Button(root, text=text, padx=138, pady=20, bg="salmon", font=('Arial', 12), command=clear)
        btn.grid(row=row, column=col, columnspan=4)
        continue
    else:
        btn = tk.Button(root, text=text, padx=20, pady=20, font=('Arial', 12), command=lambda t=text: press(t))
    btn.grid(row=row, column=col)

root.mainloop()