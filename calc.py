import tkinter as tk

def press(v):
    entry.insert(tk.END, v)

def clear():
    entry.delete(0, tk.END)

def calc():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

root = tk.Tk()
root.title("Calculator")
root.configure(bg="#1e1e1e")
root.resizable(False, False)

entry = tk.Entry(
    root,
    font=("Segoe UI", 20),
    bg="#2d2d2d",
    fg="white",
    bd=0,
    justify="right"
)
entry.grid(row=0, column=0, columnspan=4, padx=12, pady=12, ipady=10)

buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+"
]

r = 1
c = 0

for b in buttons:
    if b == "=":
        btn = tk.Button(
            root, text=b, width=5, height=2,
            font=("Segoe UI", 14),
            bg="#ff9500", fg="white",
            command=calc
        )
    elif b in ("+", "-", "*", "/"):
        btn = tk.Button(
            root, text=b, width=5, height=2,
            font=("Segoe UI", 14),
            bg="#ff9500", fg="white",
            command=lambda x=b: press(x)
        )
    else:
        btn = tk.Button(
            root, text=b, width=5, height=2,
            font=("Segoe UI", 14),
            bg="#3a3a3a", fg="white",
            command=lambda x=b: press(x)
        )

    btn.grid(row=r, column=c, padx=5, pady=5)
    c += 1
    if c > 3:
        c = 0
        r += 1

clear_btn = tk.Button(
    root, text="C", width=22, height=2,
    font=("Segoe UI", 14),
    bg="#ff453a", fg="white",
    command=clear
)
clear_btn.grid(row=r, column=0, columnspan=4, padx=5, pady=5)

root.mainloop()
