"""
Main file for lanching travtools tkinter gui
"""

import tkinter as tk
# from tkinter import ttk

# main app window config
root = tk.Tk()
root.title("Travtools App")
# root.configure(background="honeydew2")
root.minsize(600, 600)
root.geometry("300x300+50+50")

# Actions
def selection_changed(event):
    '...'
    selection = event.widget.curselection()
    if selection:
        index = selection[0]
        label.config(text=f"{event.widget.get(index)} selected!")
        event.widget.get(index)

listbox = tk.Listbox(root)
for item in ["One", "Two", "Three"]:
    listbox.insert(tk.END, item)
listbox.bind("<<ListboxSelect>>", selection_changed)
listbox.pack(padx=5, pady=5, fill="both", expand=True)



label = tk.Label(root, text="One Selected!")
label.pack(padx=5, pady=5, fill="x")

root.mainloop()
