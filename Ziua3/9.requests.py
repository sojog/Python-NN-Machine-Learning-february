import requests
import json


def fetch_a_joke():
    LINK = "https://icanhazdadjoke.com/"
    parametri = {"Accept": "application/json"} 

    response = requests.get(LINK, headers=parametri)

    print(response.status_code)
    print(response.content, type(response.content))
    print(response.text, type(response.text))

    json_response = json.loads(response.text)
    print(json_response, type(json_response))

    print("Glume este:", json_response['joke'])
    return json_response['joke']


fetch_a_joke()