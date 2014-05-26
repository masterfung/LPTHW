print 'You are at crossroad and you have to choose from three paths. What do you choose (left, middle, or right)?'

userChoice = raw_input('Please enter your choice: ')

if userChoice.lower() == 'left':
	print 'The giant zebra grabbed you and ate you like an eggplant. But all hope is not lost. You have two possible actions to try.'
	action = raw_input('Will you scream or will you cry? ')
	if action.lower() == 'scream':
		print 'The giant zebra got pissed and decided not to spare you anymore. Doom! Your end is now! Num NUM NOM'
	else:
		print 'The giant zebra saw you are sad and decided to let you go. He came back and licked you while he apologizes. You are free, he said.'

elif userChoice.lower() == 'center':
	print 'You came across three more choices, you have to eat either the berry, the cheese, or orange.'
	food = raw_input('What will you eat? (berry, cheese, or orange) ')
	if food.lower() == 'berry':
		print 'The berry turned into a frog and choked you to death. Game Over!'
	elif food.lower() == 'cheese':
		print 'You are safe and you continue to walk. Freedom ahead. :)'
	else:
		print 'That was not an orange but a tranformation potion. You are now a chili pepper. Good luck.'
else:
	print 'You are lost. Who knows. Who will?'