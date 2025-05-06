# Rajat Sharma
# CS 333 - Testing & DevOps
# Spring 2025
# Final Project - UNO!
# Used in accordance with card.py, deck.py, player.py, game.py. Main.py is not tested as it does not contain any functionality that is not already covered in the other files.

# test

from deck import Deck
from card import Card
import random


class Game:
    def __init__(self, player, ai):
        self.deck = Deck()
        self.throw = []
        self.players = [player, ai]
        self.current = 0
        self.direction = 1
        self.dealToPlayers()
        top = self.deck.draw()
        while top.value in ['Skip', 'Reverse', 'Draw Two', 'Wild Draw Four']:
            self.deck.cards.insert(0, top)
            random.shuffle(self.deck.cards)
            top = self.deck.draw()
        self.throw.append(top)

    def dealToPlayers(self):
        for playerObjs in self.players:
            playerObjs.draw(self.deck, 7)

    def topCard(self):
        return self.throw[-1]

    def getAvailableCards(self, player):
        indices = []
        top = self.topCard()
        for i, card in enumerate(player.hand):
            if card.checkEqual(top):
                indices.append(i + 1)
        return indices

    def executeCard(self, player, index, mutatedColor=None):
        card = player.play(index)
        if card.color is None and mutatedColor:
            card.color = mutatedColor
        self.throw.append(card)
        if len(player.hand) == 1:
            player.unoCheck = True
        self.applyCard(card)

    def applyCard(self, card):
        if card.value == 'Reverse':
            self.direction = -self.direction
        elif card.value == 'Skip':
            self.current = (self.current + self.direction) % len(self.players)
        elif card.value == 'Draw Two':
            nextPlayer = (self.current + self.direction) % len(self.players)
            self.players[nextPlayer].draw(self.deck, 2)
        elif card.value == 'Wild Draw Four':
            nextPlayer = (self.current + self.direction) % len(self.players)
            self.players[nextPlayer].draw(self.deck, 4)

    def setNextPlayer(self):
        self.current = (self.current + self.direction) % len(self.players)

    def getDeck(self):
        return self.deck

    def setDeck(self, deck):
        self.deck = deck

    def getDiscardPile(self):
        return self.throw

    def setDiscardPile(self, discardPile):
        self.throw = discardPile

    def getPlayers(self):
        return self.players

    def setPlayers(self, players):
        self.players = players

    def getCurrent(self):
        return self.current

    def setCurrent(self, current):
        self.current = current

    def getDirection(self):
        return self.direction

    def setDirection(self, direction):
        self.direction = direction
