import requests
import json
response = requests.get("https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1")
deckid = (response.json())['deck_id']
def getCard(numcards):
    print(requests.get('https://deckofcardsapi.com/api/deck/{id}/draw/?count={number}'.format(id = str(deckid), number = int(numcards)).dumps()))
getCard(5)