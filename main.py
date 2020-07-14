from Poker.card import Card
from Poker.deck import Deck
from Poker.game_round import GameRound
from Poker.hand import Hand
from Poker.player import Player

deck = Deck()
cards= Card.create_standard_52_cards()
deck.add_cards(cards)

hand1 = Hand()
hand2 = Hand()

player1 = Player(name = "Boris", hand = hand1)
player2 = Player(name = "Bobby", hand = hand2)
players =[player1,player2]

game_round = GameRound(deck = deck, players = players)
game_round.play()

print(player1.hand)
print(player1.best_hand())
print(player2.hand)
print(player2.best_hand())

#From main import deck, cards, game_round,hand1,hand2,player1,player2