#import random
from treys import Card
from treys import Deck
from treys import Evaluator
from player import Player
from IPython.display import clear_output

class Game():
    def __init__(self):
        self.evaluator = Evaluator()
        self.player1 = Player('player1', 10000, 'sb')
        self.player2 = Player('player2', 10000, 'bb')
        self.players = [self.player1, self.player2]
        self.pot = 0.0
        self.bb = 100
        self.sb = 50
        self.deck = Deck()
        self.board = self.deck.draw(5)
        self.player1.cards = self.deck.draw(2)
        self.player2.cards = self.deck.draw(2)
        self.player2.position = 'bb'
        
    def change_positions(self):
        if self.player1.position == 'sb':
            self.player1.position = 'bb'
            self.player2.position = 'sb'
        else:
            self.player1.position = 'sb'
            self.player2.position = 'bb'
        
    def check_winners(self):
        for player in self.players:
            if player.winner == 1:
                return True
        return False
    
    def run_game(self):
        self.change_positions()
        self.run_preflop()
        if self.check_winners == False:
            self.run_flop()
        if self.check_winners == False:
            self.run_turn()
        if self.check_winners == False:
            self.run_river()
        
        self.decide_winner()
        if self.player1.winner == 1:
            print(self.player1.name, 'has won! \n')
            self.player1.stack += self.pot
            self.pot = 0
        if self.player2.winner == 1:
            print(self.player2.name, 'has won! \n')
            self.player2.stack += self.pot
            self.pot = 0
        if self.player1.winner == 2:
            print('draw! \n')
            self.player1.stack += self.pot/2
            self.player2.stack += self.pot/2
            self.pot = 0
        self.show_board_info()
        
    #COMMAND "bet 50" to bet 50 chips
    #COMMAND "fold" to fold
    #COMMAND "call" to call
    #"check" to check
    def run_bets(self):
        over = False
        while over == False:
            print(self.players[0].name, 'type your move:')
            move = str(input()).split()
            if move[0] == 'fold':
                self.players[0].move = 'fold'
                over = True
                print(self.players[0], 'folded')
            if move[0] == 'check':
                self.players[0].move = 'check'
            if move[0] == 'call':
                if self.players[1].move[0] == 'bet':
                    self.players[0].bet(self.players[1].bet_value, self.pot)
                
            
        
    def place_blinds(self):
        print(self.players[0].name, 'placed small blind 50 \n')
        print(self.players[1].name, 'placed big blind 100 \n')
        self.players[0].bet(50, self.pot)
        self.players[1].bet(100, self.pot)
        
    def run_preflop(self):
        self.show_board_info()
        
    
    def run_flop(self):
        self.show_board_info()
        print('\n flop cards are:', Card.print_pretty_cards(self.board[:3]))
        
    def run_turn(self):
        self.show_board_info()
        print('\n turn cards are:', Card.print_pretty_cards(self.board[:4]))
    
    def run_river(self):
        self.show_board_info()
        print('\n river cards are:', Card.print_pretty_cards(self.board[:5]))
    
    def show_board_info(self):
        clear_output(wait=True)
        print('PLAYER 1 \n','stack:', self.player1.stack, '\n', 'hand:', Card.print_pretty_cards(self.player1.cards))
        print('PLAYER 2 \n','stack:', self.player2.stack, '\n', 'hand:', Card.print_pretty_cards(self.player2.cards))
        print('Pot: ', self.pot)
    
    def decide_winner(self):
        p1points = self.evaluator.evaluate(self.board, self.player1.cards)
        p2points = self.evaluator.evaluate(self.board, self.player2.cards)
        if p1points > p2points:
            self.player1.winner = 1
        elif p2points > p1points:
            self.player2.winner = 1
        else:
            self.player1.winner = self.player2.winner = 2
        
    
