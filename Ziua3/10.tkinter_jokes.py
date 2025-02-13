import tkinter as tk
import requests
import json


window = tk.Tk()

joke_label = tk.Label(window, text="Aici va fi glumea dvs..")
joke_label.pack()

# Lucru cu API
def fetch_new_joke():
    LINK = "https://icanhazdadjoke.com/"
    parametri = {"Accept": "application/json"} 
    response = requests.get(LINK, headers=parametri)
    json_response = json.loads(response.text)
    joke = json_response['joke']
    joke_label.config(text=joke)

fetch_button = tk.Button(window, text="Incearca o gluma noua!", command=fetch_new_joke)
fetch_button.pack()

window.mainloop()