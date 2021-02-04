class Player:
    def __init__(self, name, stack, position, cards = []):
        self.name = name
        self.stack = stack
        self.cards = cards
        self.position = position
        self.prev_move = ''
        self.bet_value = 0
        self.winner = 0
    def bet(self, amount, pot):
        self.stack = self.stack-amount
        pot = pot + amount
        print(self.name, 'bets:', amount)
        print('pot:', pot)
        
    def call(self, amount):
        self.stack -= amount
        
    def won(self, pot):
        self.stack += pot
        
    def fold(self, amount):
        self.cards = []
        
    def showCards(self):
        print(self.cards)
    