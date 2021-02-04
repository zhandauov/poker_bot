from treys import Card
from treys import Deck
from treys import Evaluator
from player import Player
from game import Game

player1 = Player(name = 'player1', stack = 10000, position = 'sb')
player2 = Player(name = 'player2', stack = 10000, position = 'bb')

players = [player1, player2]
players[0].stack = 50
player1.stack = 10000

game = Game()
game.run_game()

pot = 0
player1.bet(100, pot)

