# Rajat Sharma
# CS 333 - Testing & DevOps
# Spring 2025
# Final Project - UNO!
# Used in accordance with card.py, deck.py, player.py, game.py. Main.py is not tested as it does not contain any functionality that is not already covered in the other files.


class Card:
    def __init__(self, color, value):
        self.color = color
        self.value = value

    def checkEqual(self, otherCard):
        return (
            self.color is None or
            otherCard.color is None or
            self.color == otherCard.color or
            self.value == otherCard.value
        )

    def __str__(self):
        if self.color:
            return str(self.color) + ' ' + str(self.value)
        else:
            return str(self.value)
        

    def getColor(self):
        return self.color

    def setColor(self, color):
        self.color = color

    def getValue(self):
        return self.value

    def setValue(self, value):
        self.value = value
