import requests
import json
<<<<<<< HEAD

=======
>>>>>>> 330ca68b8dc2595a6098a3e43ba5f4237e2e27c9
class deckmethod:
    response = requests.get("https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1")
    discard = []
    deckid = (response.json())['deck_id']
    #takes in tuple with cardname and link to image
    def disardcard(self, card):
        self.discard.append(card)
    #draws number of cards
    def getcard(self, numcards):
        x =  (requests.get('https://deckofcardsapi.com/api/deck/' +str(self.deckid)+'/draw/?count='+str(numcards))).json()
        cardlist = []
        for card in x['cards']:
            cardlist.append((card['code'],card['image']))

        return cardlist
    #creates new deck
    def getnew(self):
        self.deckid = (requests.get("https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1").json())['deck_id']
        

<<<<<<< HEAD
a = deckmethod()
print(a.deckid)
a.getNew()
print(a.deckid)
print(a.getCard(10))
=======
>>>>>>> 330ca68b8dc2595a6098a3e43ba5f4237e2e27c9
