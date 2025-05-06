# Rajat Sharma
# CS 333 - Testing & DevOps
# Spring 2025
# Final Project - UNO!
# Used in accordance with card.py, deck.py, player.py, game.py. Main.py is not tested as it does not contain any functionality that is not already covered in the other files.

# test
# test 2


import random
from card import Card

colors = ['Red', 'Yellow', 'Green', 'Blue']
values = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'Skip', 'Reverse', 'Draw Two']
specialCards = ['Wild', 'Wild Draw Four']

class Deck:
    def __init__(self):
        self.cards = self.makeDeck()
        random.shuffle(self.cards)

    def makeDeck(self):
        cards = []
        for color in colors:
            cards.append(Card(color, '0'))
            for value in values[1:]:
                cards.append(Card(color, value))
                cards.append(Card(color, value))
        for i in range(4):
            cards.append(Card(None, 'Wild'))
            cards.append(Card(None, 'Wild Draw Four'))
        return cards

    def draw(self):
        if not self.cards:
            print("Deck is empty!")
            return None
        return self.cards.pop()

    def getLength(self):
        return len(self.cards)

    def getCards(self):
        return self.cards

    def setCards(self, cards):
        self.cards = cards
