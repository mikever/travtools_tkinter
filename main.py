"""
Main file for lanching travtools tkinter gui
"""

import tkinter as tk

# main app window
root = tk.Tk()
root.title("Travtools App")
root.configure(background="honeydew2")
root.minsize(600, 600)
# root.maxsize(500, 500)
root.geometry("300x300+50+50")

# add a label widget to root and pack with y-padding
tk.Label(root, text="Hello, Python GUI!").pack(pady=20)
tk.Label(root, text="An Image below:").pack()

image = tk.PhotoImage(file="guitar-small.png")
tk.Label(root, image=image).pack()

root.mainloop()
