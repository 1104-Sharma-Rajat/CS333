# Rajat Sharma
# CS 333 - Testing & DevOps
# Spring 2025
# Final Project - UNO!
# Used in accordance with card.py, deck.py, player.py, game.py. Main.py is not tested as it does not contain any functionality that is not already covered in the other files.

# test update

import unittest
from card import Card
from deck import Deck, colors, values, specialCards
from player import Player
from game import Game

class UnitTests(unittest.TestCase):
    # Unit tests for the Card class
    def test_cardSetup(self):
        newCard = Card('Blue', '4')
        self.assertEqual(newCard.color, 'Blue')
        self.assertEqual(newCard.value, '4')

     # Unit tests for the Card class
    def test_cardToString(self):
        newCard = Card('Blue', '4')
        self.assertEqual(str(newCard), 'Blue 4')

     # Unit tests for the Card class
    def test_cardToStringWild(self):
        newCard = Card(None, 'Wild')
        self.assertEqual(str(newCard), 'Wild')

     # Unit tests for the Card class
    def test_cardCheckEqualByMatchingColor(self):
        newCard = Card('Blue', '4')
        newCard2 = Card('Blue', '5')
        self.assertTrue(newCard.checkEqual(newCard2))
        self.assertTrue(newCard2.checkEqual(newCard))

     # Unit tests for the Card class
    def test_cardCheckEqualByMatchingValue(self):
        newCard = Card('Blue', '4')
        newCard2 = Card('Red', '4')
        self.assertTrue(newCard.checkEqual(newCard2))
        self.assertTrue(newCard2.checkEqual(newCard))
    
     # Unit tests for the Card class
    def test_cardCheckEqualByWildCard(self):
        newCard = Card('Blue', '4')
        newCard2 = Card(None, 'Wild')
        self.assertTrue(newCard.checkEqual(newCard2))
        self.assertTrue(newCard2.checkEqual(newCard))

     # Unit tests for the Deck class
    def test_deckSetup(self):
        newDeck = Deck()
        self.assertEqual(len(newDeck.cards), 108)

     # Unit tests for the Deck class
    def test_deckDrawCard(self):
        newDeck = Deck()
        ogLength = len(newDeck.cards)
        newCard = newDeck.draw()
        self.assertEqual(len(newDeck.cards), ogLength - 1)

     # Unit tests for the Deck class
    def test_deckDrawEmpty(self):
        newDeck = Deck()
        newDeck.cards = []
        newCard = newDeck.draw()
        self.assertIsNone(newCard)
    
     # Unit tests for the Player class
    def test_playerSetup(self):
        newPlayer = Player('Player')
        self.assertEqual(newPlayer.name, 'Player')
        self.assertEqual(len(newPlayer.hand), 0)
        self.assertFalse(newPlayer.isUno)
    
     # Unit tests for the Player class
    def test_playerPlayCard(self):
        newPlayer = Player('Bob')
        newDeck = Deck()
        newPlayer.draw(newDeck, 7)
        ogLength = len(newPlayer.hand)
        newCard = newPlayer.play(1)
        self.assertEqual(len(newPlayer.hand), ogLength - 1)
        
     # Integration Test #1
    def test_integrationGameSetup(self):
        newDeck = Deck()
        newPlayer = Player('Bob')
        newAI = Player('AI')

        newGame = Game(newPlayer, newAI)

        self.assertEqual(len(newGame.throw), 1)
        self.assertEqual(len(newPlayer.hand), 7)
        self.assertEqual(len(newAI.hand), 7)
        self.assertEqual(newGame.current, 0)
        self.assertEqual(newGame.direction, 1)

    # Integration Test #2
    def test_integrationGetAvailableCards(self):
        newPlayer = Player('Bob')
        newAI = Player('AI')

        newGame = Game(newPlayer, newAI)

        topCardTest = Card('Red', '9')
        newGame.throw = [topCardTest]

        newPlayer.hand = [Card('Red', '5'), Card('Blue', '3'), Card('Green', '9')]
        availableCards = newGame.getAvailableCards(newPlayer)

        self.assertIn(1, availableCards) 
        self.assertIn(3, availableCards)
        self.assertNotIn(2, availableCards)

    # Integration Test #3
    def test_integrationSkip(self):
        newPlayer = Player('Bob')
        newAI = Player('AI')
        game = Game(newPlayer, newAI)
        game.current = 0

        newPlayer.hand = [Card('Yellow', 'Skip')]
        game.executeCard(newPlayer, 0)
        self.assertEqual(game.current, 1)

    # Integration Test #4
    def test_integrationSetNext(self):
        newPlayer = Player('Bob')
        newAI = Player('AI')
        game = Game(newPlayer, newAI)
        game.current = 0
        game.direction = 1

        game.setNextPlayer()
        self.assertEqual(game.current, 1)

        game.setNextPlayer()
        self.assertEqual(game.current, 0)
    
    # Integration Test #5
    def test_integrationWildDrawFour(self):
        newPlayer = Player('Bob')
        newAI = Player('AI')
        game = Game(newPlayer, newAI)
        game.current = 0
        game.direction = 1
        ogSize = len(newAI.hand)

        newPlayer.hand = [Card(None, 'Wild Draw Four')]
        game.executeCard(newPlayer, 0)
        self.assertEqual(len(newAI.hand), ogSize + 4)

    # Integration Test #6
    def test_integrationDrawTwo(self):
        newPlayer = Player('Bob')
        newAI = Player('AI')
        game = Game(newPlayer, newAI)
        game.current = 0
        game.direction = 1
        ogSize = len(newAI.hand)

        newPlayer.hand = [Card('Red', 'Draw Two')]
        game.executeCard(newPlayer, 0)
        self.assertEqual(len(newAI.hand), ogSize + 2)

    # Integration Test #7
    def test_integrationReverse(self):
        newPlayer = Player('Bob')
        newAI = Player('AI')
        game = Game(newPlayer, newAI)
        game.current = 0
        game.direction = 1

        newPlayer.hand = [Card('Red', 'Reverse')]
        game.executeCard(newPlayer, 0)
        self.assertEqual(game.direction, -1)

        


