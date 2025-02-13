
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

increment = 0
def printeaza_in_consola():
    global increment
    increment += 1
    print(f"Butonul a fost apasat de {increment} ori")

button = tk.Button(window, text="Apasa-ma???",command=printeaza_in_consola)
button.pack()

window.mainloop()