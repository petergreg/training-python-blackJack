'''
File for base function to play game
'''

def take_bet(chips):
	print(('You have {} chips.').format(chips.total))
	while True:
		try:
			chips.bet = int(input('How many chips would you like to bet? '))
		except:
			print('Sorry, please provide an integer')
		else:
			if chips.bet > chips.total:
				print('Sorry, you do not have enough chips! You have: {}'.format(chips.total))
			else:
				break

def hit(deck, hand):
	single_card = deck.deal()
	hand.add_card(single_card)
	hand.adjust_for_aces()

def hit_or_stand(deck, hand):
	global playing # To control while loop

	while(True):
		x = input('\nHit or Stand? enter h or s ')
		if x[0].lower() == 'h':
			print("\n-- Hitting.")			
			hit(deck, hand)
			return True
		elif x[0].lower() == 's':
			print("\n-- Standing. \nDearler's turn")
			return False
		else:
			print('Sorry, I did not understand that, please enter h or s.')
			continue
		break

def show_some(player, dealer):
	print('\nDEALERS HAND:')
	print('one card hidden!')
	print(dealer.cards[1])
	print('\n')
	print('PLAYERS HAND:')
	for card in player.cards:
		print(card)

def show_all(player, dealer):
	print('\nDEALERS HAND:')
	for card in dealer.cards:
		print(card)
	print('\n')
	print('PAYERS HAND:')
	for card in player.cards:
		print(card)

def player_busts(player, dealer, chips):
	print("\n--> BUST PLAYER!")
	chips.lose_bet() 

def player_wins(player, dealer, chips):
	print("\n--> PLAYER WINS")
	chips.win_bet()

def dealer_busts(player, dealer, chips):
	print("\n--> PLAYER WINS! DEALER BUSTED!")
	chips.win_bet()

def dealer_wins(player, dealer, chips):
	print("\n--> DEALER WINS")
	chips.lose_bet()

def push(player, dealer):
	print('\n--> Dealer and player tie! PUSH')

