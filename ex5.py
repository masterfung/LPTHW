firstName = 'Johnny'
lastName = 'Hung'
location = 'United States'
year = 2014
one = 123
two = 567

print 'Hi my first name is: %s and my last name is: %s.' % (firstName, lastName)
print 'His location is the %s and this year is %s. His magical number is: %s.' % (location, year, one + two)
print '{} {} is from the {} where this year: {} will produce this lucky number {}.'.format(firstName, lastName, location, year, one + two)