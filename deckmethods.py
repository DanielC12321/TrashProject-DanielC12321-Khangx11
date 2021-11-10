import requests
import json
<<<<<<< HEAD
response = requests.get("https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1")
deckid = (response.json())['deck_id']
def getCard(numcards):
    print(requests.get('https://deckofcardsapi.com/api/deck/{id}/draw/?count={number}'.format(id = str(deckid), number = int(numcards)).dumps()))
getCard(5)
=======
class deckmethod:
    response = requests.get("https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1")
    
    deckid = (response.json())['deck_id']
    def getCard(self, numcards):
        x =  (requests.get('https://deckofcardsapi.com/api/deck/' +str(self.deckid)+'/draw/?count='+str(numcards))).json()
        cardlist = []
        for card in x['cards']:
            cardlist.append((card['code'],card['image']))

        return cardlist

    def getNew(self):
        self.deckid = (requests.get("https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1").json())['deck_id']
        pass



a = deckmethod()
print(a.deckid)
a.getNew()
print(a.deckid)
print(a.getCard(10))
>>>>>>> 709e46517e5c5270314a3e9aea619bcfe3c929e3
