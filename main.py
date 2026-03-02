"""
Main file for lanching travtools tkinter gui

The Scale widget provides a slide-bar that works much like a Spinbox.
Rather than displaying the current value numerically, it displays the position of the slider handle along the length of the widget.
"""

import tkinter as tk

# main app window config
root = tk.Tk()
root.title("Travtools App")
root.configure(background="honeydew2")
root.minsize(600, 600)
root.geometry("300x300+50+50")


# Actions
def value_changed(event):
    label.config(text=event.widget.get())


scale = tk.Scale(root, from_=0, to=10, orient="horizontal")
scale.bind("<Motion>", value_changed)
scale.pack(padx=5, pady=5, fill="x")

# helper label to show the selected value
label = tk.Label(root, text="0")
label.pack(padx=5, pady=5, fill="x")

root.mainloop()
