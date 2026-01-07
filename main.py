import tkinter as tk

# main app window
window = tk.Tk()
window.title("Travtools App")
window.geometry("300x200")

# add a label widget
label = tk.Label(window, text="Hello, Python GUI!")
label.pack(pady=20) # Add the label to the window

# start the GUI event loop
window.mainloop()
