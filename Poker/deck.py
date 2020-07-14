import random 
from Poker.card import Card


class Deck():
    def __init__(self):
        self.cards =[]

    def __len__(self):
        return len(self.cards)

    def add_cards(self,cards):
        self.cards.extend(cards)

    def shuffle(self):
        random.shuffle(self.cards)

    def remove_cards(self,number):
        cards_to_remove = self.cards[:number]
        del self.cards[:number]
        return cards_to_remove

    def create_card(self):
        cards = []