import tkinter as tk
from tkinter import messagebox
import random

# === Global theme and state ===
dark_mode = False

# === Roll logic ===
def roll_dice(num_dice, die_type, modifier):
    rolls = [random.randint(1, die_type) for _ in range(num_dice)]
    total = sum(rolls) + modifier
    return rolls, total

# === Roll handler ===
def on_roll_button():
    try:
        num_dice = int(num_dice_entry.get())
        modifier = int(modifier_entry.get()) if modifier_entry.get() else 0
        die_type = int(selected_die.get())
        if num_dice <= 0 or die_type <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers for dice, die type, and modifier.")
        return

    rolls, total = roll_dice(num_dice, die_type, modifier)
    result_text.set(f"🎲 Rolls: {rolls}\nModifier: {modifier}\nTotal: {total}")

# === Dark Mode toggle ===
def toggle_dark_mode():
    global dark_mode
    dark_mode = not dark_mode
    apply_theme()

def apply_theme():
    bg = "#1e1e1e" if dark_mode else "#ffffff"
    fg = "#f0f0f0" if dark_mode else "#000000"
    entry_bg = "#2c2c2c" if dark_mode else "#ffffff"

    root.config(bg=bg)
    for widget in root.winfo_children():
        if isinstance(widget, (tk.Label, tk.Button, tk.OptionMenu)):
            widget.config(bg=bg, fg=fg, activebackground=bg, activeforeground=fg)
        elif isinstance(widget, tk.Entry):
            widget.config(bg=entry_bg, fg=fg, insertbackground=fg)
        elif isinstance(widget, tk.Frame):
            widget.config(bg=bg)
            for child in widget.winfo_children():
                if isinstance(child, tk.Button):
                    child.config(bg=bg, fg=fg, activebackground=bg, activeforeground=fg)

# === GUI Setup ===
root = tk.Tk()
root.title("🎲 Dice Roller App")
root.geometry("300x450")
root.resizable(False, False)

# Input for number of dice
tk.Label(root, text="Number of Dice:").pack(pady=5)
num_dice_entry = tk.Entry(root)
num_dice_entry.insert(0, "1")
num_dice_entry.pack()

# Input for modifier
tk.Label(root, text="Modifier (+/-):").pack(pady=5)
modifier_entry = tk.Entry(root)
modifier_entry.insert(0, "0")
modifier_entry.pack()

# Dropdown for die type
tk.Label(root, text="Select Die Type:").pack(pady=10)
selected_die = tk.StringVar(root)
selected_die.set("6")  # Default is D6
die_options = ["4", "6", "8", "10", "12", "20", "100"]
die_dropdown = tk.OptionMenu(root, selected_die, *die_options)
die_dropdown.pack()

# Roll button
tk.Button(root, text="🎲 Roll Dice", command=on_roll_button).pack(pady=15)

# Result label
result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text, wraplength=250, justify="center", fg="blue")
result_label.pack(pady=20)

# Extra controls
tk.Button(root, text="Toggle Dark Mode 🌙", command=toggle_dark_mode).pack(pady=5)
tk.Button(root, text="Quit", command=root.destroy).pack(pady=10)

apply_theme()
root.mainloop()
