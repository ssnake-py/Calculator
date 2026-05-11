import tkinter as tk
import math
from fractions import Fraction

# logika
def click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(value))

def clear():
    entry.delete(0, tk.END)

def sqrt():
    try:
        value = eval_expression(entry.get())
        result = math.sqrt(float(value))
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# zamiana na ułamki
def eval_expression(expr):
    return eval(expr, {"Fraction": Fraction, "sqrt": math.sqrt})

def calculate():
    try:
        result = eval_expression(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")


# okno
root = tk.Tk()
root.title("Calculator")
root.geometry("320x450")
root.resizable(False, False)

entry = tk.Entry(root, font=("Arial", 18), justify="right")
entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

# przyciski
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+"
]

frame = tk.Frame(root)
frame.pack()

row = 0
col = 0

for b in buttons:
    if b == "=":
        btn = tk.Button(frame, text=b, width=5, height=2, command=calculate)
    else:
        btn = tk.Button(frame, text=b, width=5, height=2,
                        command=lambda x=b: click(x))

    btn.grid(row=row, column=col)

    col += 1
    if col > 3:
        col = 0
        row += 1


# extra
extra = tk.Frame(root)
extra.pack(pady=5)

tk.Button(extra, text="√", width=10, command=sqrt).pack(side="left", padx=5)
tk.Button(extra, text="Clear", width=10, command=clear).pack(side="left", padx=5)

root.mainloop()
