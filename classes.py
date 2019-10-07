import random

'''
Listing values for cards
'''
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
values = {'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':10,'Queen':10,'King':10,'Ace':11}


'''
Class for cards
'''
class Card:

	def __init__(self,suit,rank):
		self.suit = suit
		self.rank = rank

	def __str__(self):
		return self.rank + " of " + self.suit

'''
Class for the deck of cards.
'''
class Deck:

	def __init__(self):
		self.deck = []
		for suit in suits:
			for rank in ranks:
				self.deck.append(Card(suit, rank))

	def __str__(self):
		deck_composition = ''
		for card in self.deck:
			deck_composition += '\n' + card.__str__()
		return 'The deck has: ' + deck_composition

	def shuffle(self):
		random.shuffle(self.deck)

	def deal(self):
		return self.deck.pop()

'''
Hand of the player
'''
class Hand:

	def __init__(self):
		self.cards = []
		self.value = 0
		self.aces = 0

	'''
	Adding a card to the hand
	'''
	def add_card(self, card):
		self.cards.append(card)
		self.value += values[card.rank]

		# Keeping track of aces
		if card.rank == 'Ace':
			self.aces += 1

	def adjust_for_aces(self):
		# If total value > 21 and still have an ace, than change
		# the Ace to be a 1 instead of an 11
		while self.value < 21 and self.aces:
			self.value -= 10
			self.aces -= 1

'''
Class to manage chips and bets
'''
class Chips:

	def __init__(self, total=100):
		self.total = total
		self.bet = 0

	def win_bet(self):
		self.total += self.bet

	def lose_bet(self):
		self.total -= self.bet




