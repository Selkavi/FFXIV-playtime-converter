import tkinter as tk
from tkinter import messagebox

def calculate_hours():
    try:
        total_days = int(entry_days.get())
        total_hours = int(entry_hours.get())
        total_minutes = int(entry_minutes.get())

        total_playtime = total_days * 24 + total_hours + total_minutes / 60
        messagebox.showinfo("Result", f"Okay, Nerd. You played {total_playtime:.2f} hours lmao.")
    except ValueError:
        messagebox.showerror("Error", "Please enter numbers only!")

# Fenster erstellen
root = tk.Tk()
root.title("FFXIV Playtime Calculator")

tk.Label(root, text="Play Days >⩊<").pack()
entry_days = tk.Entry(root)
entry_days.pack()

tk.Label(root, text="Play Hours ⋆˚࿔").pack()
entry_hours = tk.Entry(root)
entry_hours.pack()

tk.Label(root, text="Play Minutes ୨ৎ").pack()
entry_minutes = tk.Entry(root)
entry_minutes.pack()

tk.Button(root, text="Calculate", command=calculate_hours).pack()

root.mainloop()
