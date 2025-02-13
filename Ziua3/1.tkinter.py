
import tkinter as tk

window = tk.Tk()

WIDTTH = 500
HEIGHT = 1000
X = 20
Y = 30

window.geometry(f"{WIDTTH}x{HEIGHT}+{X}+{Y}")

window.mainloop()