
import tkinter as tk

window = tk.Tk()

WIDTTH  =  HEIGHT = 500

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

print("Ecranul are width:", screen_width, "height:", screen_height)
X = screen_width // 2 - WIDTTH // 2
Y = screen_height // 2 - HEIGHT // 2

window.geometry(f"{WIDTTH}x{HEIGHT}+{X}+{Y}")

window.mainloop()