"""
Main file for lanching travtools tkinter gui
"""

import tkinter as tk

# main app window config
root = tk.Tk()
root.title("Travtools App")
root.configure(background="honeydew2")
root.minsize(600, 600)
root.geometry("300x300+50+50")


# Actions
def return_pressed(event):
    label.config(text=event.widget.get())


entry = tk.Entry(root)
entry.insert(0, "Enter your text")
entry.bind("<Return>", return_pressed)
entry.pack(padx=5, pady=5, fill="x")


# helper label to show the selected value
label = tk.Label(root, text="Entry demo!")
label.pack(padx=5, pady=5, fill="x")

root.mainloop()
