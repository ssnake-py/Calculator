import tkinter as tk

# logika
def click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(value))

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# okno
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")
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

clear_btn = tk.Button(root, text="Clear", width=10, height=2, command=clear)
clear_btn.pack(pady=10)

root.mainloop()
