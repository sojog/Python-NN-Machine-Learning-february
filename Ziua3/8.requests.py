# pip install requests

import requests

LINK = "https://nn.ro/"

response = requests.get(LINK)
print(response.status_code)
print(response.content[:100])

with open("nn.html", "w") as fwriter:
    fwriter.write(response.text)