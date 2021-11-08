import requests
import json
response = requests.get("https://deckofcardsapi.com/api/deck/new/draw/?count=10")
x = response.json()
print(response.status_code)
print(json.dumps(response.json(),indent=4) )
for card in x['cards']:
    print(card['code'])
    print(card['image'])
