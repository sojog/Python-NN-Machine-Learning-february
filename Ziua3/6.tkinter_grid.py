import tkinter as tk

window = tk.Tk()

WIDTTH  =  HEIGHT = 500

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
X = screen_width // 2 - WIDTTH // 2
Y = screen_height // 2 - HEIGHT // 2
window.geometry(f"{WIDTTH}x{HEIGHT}+{X}+{Y}")

counter = 0
def aduna_valoare(val):
    global counter
    counter += val
    print("Counterul este la :", counter)
    counter_label.config(text=f"{counter}")

minus_button = tk.Button(window, text="-", command=lambda x=-1:aduna_valoare(x))
minus_button.grid(row=0, column=0)

counter_label = tk.Label(window, text=f"{counter}")
counter_label.grid(row=0, column=1)

plus_button = tk.Button(window, text="+", command=lambda x=1:aduna_valoare(x))
plus_button.grid(row=0, column=2)



window.mainloop()