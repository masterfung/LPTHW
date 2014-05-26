series = [5, 6, 7, 8, 9, 0, 1, 2, 3, 4]
colors = ['red', 'blue', 'green', 'white', 'yellow', 'black']
directions = ['top', 'right', 'left', 'bottom', 'center', 'behind']

for number in series:
	print 'The numbers are as follow: %d' % number

for beauty in colors:
	print 'So many colors but here are what stand out most: %s.' % beauty

progress = []

for i in range (0, 100):
	print 'There are so many countries. Counting now. Process to completion: %d' % i
	progress.append(i)

for signs in directions:
	print 'Do no fear. We are here to help you through this challenge.', 'Please follow this exactly as ordered to get out of this evil forest safely: %s. Please hurry or else you will be eaten by seaweed!' % signs