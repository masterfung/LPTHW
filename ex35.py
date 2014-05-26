from sys import exit
def treasure():
	print 'You landed on top of the treasure room. How much do you take?'
	userInput = int(raw_input('Let me know: '))
	if userInput <= 0:
		userInput = int(raw_input('Let me know: '))
	elif userInput < 100:
		print 'You are not greedy. You may exit this chamber unharmed!'
		exit(0)
	else:
		dead('WOW! Greedy! Off with his head!')

def doom():
	print 'This is doom. You aready?'
	answer = raw_input('Answer: Yes or No now. ')
	if answer.lower() == 'yes':
		print 'Prepare for battle!'
		print 'You look around the room and saw three weapons: sword, mace, and hook. Which weapon do you reach for?'
		weapon = raw_input('> ')
		if weapon.lower() == 'sword':
			print 'The rusty blade could not stand up against the dark lord! Your blood has been spilled.',
			dead('Bye now!')
		elif weapon.lower() == 'mace':
			print 'Do you really think the mace can stand against the might dark lord? You are finished!'
			dead('Wow you are weak!')
		elif weapon.lower() == 'hook':
			print 'This confuses the dark lord, he likes your creativitiy. Free!'
			exit(0)
		else:
			print 'Luck is not with you and your head is off. Bye!'
			dead()
	else:
		print 'Weakling! Death arrives at your doorstep.'
		dead('You are shamed!')

def dead(reason):
	print reason, 'Good job pal!'
	exit(0)

def start():
	print 'You are in a dark room and you have to choose either the left room or the right room, which will you choose?'
	choice = raw_input('Your choice: ')
	if choice.lower() == 'left':
		treasure()
	elif choice.lower() == 'right':
		doom()
	else:
		dead('Your foolishness means your doom!')

start()