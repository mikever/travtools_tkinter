"""
Main file for lanching travtools tkinter gui
"""

import tkinter as tk
from tkinter import ttk

# main app window config
root = tk.Tk()
root.title("Travtools App")
# root.configure(background="honeydew2")
root.minsize(600, 600)
root.geometry("300x300+50+50")

# Actions
def selection_changed(event):
    '...'
    label.config(text=f"{event.widget.get()} selected!")


combobox = ttk.Combobox(root, values=["One", "Two", "Three"])
combobox.set("One")
combobox.bind("<<ComboboxSelected>>", selection_changed)
combobox.pack(padx=5, pady=5, fill="x")

label = tk.Label(root, text="One Selected!")
label.pack(padx=5, pady=5, fill="x")

root.mainloop()
