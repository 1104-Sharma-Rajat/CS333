# Rajat Sharma
# CS 333 - Testing & DevOps
# Spring 2025
# Final Project - UNO!
# Used in accordance with card.py, deck.py, player.py, game.py. Main.py is not tested as it does not contain any functionality that is not already covered in the other files.


# test 
class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.isUno = False

    def draw(self, deck, count = 1):
        for i in range(count):
            self.hand.append(deck.draw())

    def play(self, index):
        return self.hand.pop(index)

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getHand(self):
        return self.hand

    def setHand(self, hand):
        self.hand = hand

    def getIsUno(self):
        return self.isUno

    def setIsUno(self, isUno):
        self.isUno = isUno
