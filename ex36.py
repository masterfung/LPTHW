userGenerated = []

first = raw_input('What is your first name? ')
userGenerated.append(first)
second = raw_input('What is your last name? ')
userGenerated.append(second)
third = int(raw_input('What is your favorite number? '))
userGenerated.append(third)
fourth = raw_input('What is your favorite TV show? ')
userGenerated.append(fourth)
fifth = raw_input('Name your favorite color? ')
userGenerated.append(fifth)

for i in userGenerated:
	print i

print 'I am {} {} and I love the show called: {}. My favorite color is: {} and my favorite number is: {}.'.format(userGenerated[0], userGenerated[1], userGenerated[3], userGenerated[4], userGenerated[2])