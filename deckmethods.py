import requests
import json
response = requests.get("https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1")
deckid = (response.json())['deck_id']
def getCard(numcards):
    print(requests.get('https://deckofcardsapi.com/api/deck/{id}/draw/?count={number}'.format(id = String(deckid), number = int(numcards)).dumps())
    pass