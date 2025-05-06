# Rajat Sharma
# CS 333 - Testing & DevOps
# Spring 2025
# Final Project - UNO!
# Used in accordance with card.py, deck.py, player.py, game.py. 

# This file is not tested as it does not contain any functionality that is not already covered in the other files.
# This file only contains I/O functionality.

# test
# test 2

from deck import *
from game import *
from player import *
from card import *

def main():
    player = Player('Player')
    ai = Player('AI')
    game = Game(player, ai)

    while True:


        current = game.players[game.current]
        topOfStack = game.topCard()
        if current is player:
            print("Last Played:", topOfStack)
            print()
            print("Hand:")

            for playCardInput, card in enumerate(player.hand, 1):
                print(playCardInput, card)

            playableCardNums = game.getAvailableCards(player)
            print("Playable Cards: ", playableCardNums)
            choice = input("Select card index or 'D' to draw: ")
            if choice == 'd' or choice == 'D':
                player.draw(game.deck)
                print("Drawing a card!")
            else:
                try:
                    playCardInput = int(choice)
                    if playCardInput in playableCardNums:
                        card = player.hand[playCardInput - 1]
                        mutatedColor = None
                        if card.color is None:
                            mutatedColor = input("Choose a color: " + str(colors) + ": ").strip().title()
                        game.executeCard(player, playCardInput - 1, mutatedColor)

                        print("You played: ", game.topCard())
                        if player.isUno:
                            print("You say UNO! :O")
                    else:
                        print("Invalid input. Drawing a card! :(")
                        player.draw(game.deck)      
                except:
                    print("Invalid input. Drawing a card! :(")
                    player.draw(game.deck)
        else:
            playableCardNums = game.getAvailableCards(ai)
            if playableCardNums:
                playCardInput = random.choice(playableCardNums) - 1
                card = ai.hand[playCardInput]
                mutatedColor = None
                if card.color is None:

                    mutatedColor = random.choice(colors)
                game.executeCard(ai, playCardInput, mutatedColor)
                print("AI played: ", game.topCard())
                if ai.isUno:
                    print("AI says UNO! :O")
            else:
                ai.draw(game.deck)
                print("AI draws a card!")

        if not current.hand:
            print(current.name, "wins!")
            break
        game.setNextPlayer()

if __name__ == '__main__':
    main()
