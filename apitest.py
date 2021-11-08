import requests
import json
response = requests.get("https://deckofcardsapi.com/api/deck/new/draw/?count=2")
print(response.status_code)
print(json.dumps(response.json(),indent=4) )
