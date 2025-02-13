
import tkinter as tk

window = tk.Tk()

WIDTTH  =  HEIGHT = 500

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
X = screen_width // 2 - WIDTTH // 2
Y = screen_height // 2 - HEIGHT // 2
window.geometry(f"{WIDTTH}x{HEIGHT}+{X}+{Y}")

label1 = tk.Label(window, text="Label-ul meu... din fereastra mea")
label1.pack()


label2 = tk.Label(window, text="Un alt label al meu... din fereastra mea")
label2.pack()


label_list = []
for i in range(100):
    new_label = tk.Label(window, text=f"Label cu nr {i+1}... din fereastra mea")
    new_label.pack()
    label_list.append(new_label)

# window.resizable(False, False)

scroll_bar = tk.Scrollbar(window) 
scroll_bar.pack( side = tk.RIGHT ) 


window.mainloop()