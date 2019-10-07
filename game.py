'''
Python file to start game
'''
import classes
import actions

playing = True
player_chips = classes.Chips()



while True:
	print('\n\n--- WELCOME TO BLACKJACK ---\n')

	deck = classes.Deck()
	deck.shuffle()

	# Initializing hands
	player_hand = classes.Hand()
	player_hand.add_card(deck.deal())
	player_hand.add_card(deck.deal())

	dealer_hand = classes.Hand()
	dealer_hand.add_card(deck.deal())
	dealer_hand.add_card(deck.deal())

	# Setting chips
	actions.take_bet(player_chips)

	# Showing cards
	actions.show_some(player_hand, dealer_hand)

	while playing:

		playing = actions.hit_or_stand(deck, player_hand)
		actions.show_some(player_hand, dealer_hand)

		if player_hand.value > 21:
			actions.player_busts(player_hand, dealer_hand, player_chips)
			break

	# If player hasn't busted, play dealer's hand until value > player's
	if player_hand.value <= 21 :

		while dealer_hand.value < player_hand.value:
			actions.hit(deck, dealer_hand)

		# Show all cards
		actions.show_all(player_hand, dealer_hand)

		# Run differen winning scenarios
		if dealer_hand.value > 21:
			actions.dealer_busts(player_hand, dealer_hand, player_chips)
		elif dealer_hand.value > player_hand.value:
			actions.dealer_wins(player_hand, dealer_hand, player_chips)
		elif dealer_hand.value < player_hand.value:
			actions.player_wins(player_hand, dealer_hand, player_chips)
		else:
			actions.push(player_hand, dealer_hand)

	print('\n Player total chips are at: {}'.format(player_chips.total))
	new_game = input("Would you like to play another hand? y/n ")
	print(new_game[0])

	if new_game[0].lower() == 'y':
		playing = True
		continue
	else:
		print('Thank you for playing!')
		break
