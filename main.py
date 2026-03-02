"""
Main file for lanching travtools tkinter gui

The Spinbox widget provides an input box for numerical values. It has arrows to increase and decrease the value.
"""

import tkinter as tk

# main app window config
root = tk.Tk()
root.title("Travtools App")
root.configure(background="honeydew2")
root.minsize(600, 600)
root.geometry("300x300+50+50")


# Actions
spinbox_var = tk.StringVar(value="0")
spinbox = tk.Spinbox(
    root,
    from_=-10,
    to=10,
    textvariable=spinbox_var,
)
spinbox.pack(padx=5, pady=5, fill="x")

# helper label to show the selected value
label = tk.Label(root, textvariable=spinbox_var)
label.pack(padx=5, pady=5, fill="x")

root.mainloop()
