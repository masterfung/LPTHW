structure = '%s %s %s %s %s'

print structure % (1, 5, 6, 10, 100)
print structure % ('land before', 'time', 'is', 'like the best', 'show ever')
print structure % (True, 'is', 'always better', 'than', False )
print structure % (structure, structure, structure, structure, structure)
print structure % (
	'Once Upon a Time',
	'Game of Thrones',
	'Arrow',
	'The Flash',
	'Mythbusters')