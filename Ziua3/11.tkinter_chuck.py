import tkinter as tk
import requests
import json


window = tk.Tk()

input = tk.Entry(window)
input.pack()

joke_label = tk.Label(window, text="Aici va fi glumea dvs..")
joke_label.pack()

# Lucru cu API
def fetch_new_joke():
    LINK = "https://api.chucknorris.io/jokes/search"
    parametri = {"Accept": "application/json"} 

    search_term  = input.get()

    response = requests.get(LINK, headers=parametri, params={"query" : search_term})
    json_response = json.loads(response.text)
    print(json_response)
    results = json_response['result']
    if results:
        joke = results[0]['value']
        joke_label.config(text=joke)
    else:
        joke_label.config(text="Esti o gluma...")

fetch_button = tk.Button(window, text="Incearca o gluma noua!", command=fetch_new_joke)
fetch_button.pack()

window.mainloop()