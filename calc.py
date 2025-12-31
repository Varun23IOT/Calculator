import tkinter as tk
from tkinter import ttk
import re

root = tk.Tk()
root.title("Calculator")
root.resizable(False, False)
root.geometry("320x420+100+200")
root.configure(bg="#FFFDD0")

style = ttk.Style()
style.theme_use("clam")
style.configure("Calc.TButton", background="white", foreground="brown",padding=10,font=("Arial",12,"bold"))
style.map("Calc.TButton", background=[("active", "orange"), ("pressed", "white")])
style.configure("Clear.TButton", background="#FF3B3B", foreground="white",font=("Arial",12,"bold"))
style.map("Clear.TButton", background=[("active", "#FF6B6B"), ("pressed", "#D92B2B")])
style.configure("Calc.TEntry", fieldbackground="black", foreground="white")

display = ttk.Entry(root, font=("Arial", 20), justify="right", style="Calc.TEntry")
display.grid(row=0, column=0, columnspan=4, sticky="nsew")

buttons = [
    ["C", "/", "* ",  "<"],
    ["7", "8", "9 ",  "-"],
    ["4", "5", "6 ",  "+"],
    ["1", "2", "3 ",  "."],
    ["%", "0", "//",  "="],
]

def apply_percent():
    expr = display.get()
    match = re.search(r'(\d+\.?\d*)$', expr)
    if match:
        num = match.group(1)
        percent = str(float(num) / 100)
        display.delete(len(expr) - len(num), tk.END)
        display.insert(tk.END, percent)

def click(value):
    if value == "C":
        display.delete(0, tk.END)

    elif value == "<":
        display.delete(len(display.get()) - 1, tk.END)

    elif value == "%":
        apply_percent()

    elif value == "=":
        try:
            result = eval(display.get())
            display.delete(0, tk.END)
            display.insert(tk.END, str(result))
        except:
            display.delete(0, tk.END)
            display.insert(tk.END, "Error")

    else:
        display.insert(tk.END, value)

for r in range(1, 6):
    for c in range(4):
        text = buttons[r-1][c]
        if text == " ":
            continue

        if text == "=":
            btn = ttk.Button(root, text="=", style="Calc.TButton",
                             command=lambda t="=": click(t))
            btn.grid(row=r, column=c, rowspan=2, sticky="nsew", padx=2, pady=2)

        elif text == "C":
            btn = ttk.Button(root, text=text, style="Clear.TButton",
                             command=lambda t=text: click(t))
            btn.grid(row=r, column=c, sticky="nsew", padx=2, pady=2)

        else:
            btn = ttk.Button(root, text=text, style="Calc.TButton",
                             command=lambda t=text: click(t))
            btn.grid(row=r, column=c, sticky="nsew", padx=2, pady=2)

for i in range(4):
    root.grid_columnconfigure(i, weight=1)

for i in range(6):
    root.grid_rowconfigure(i, weight=1)

root.mainloop()
