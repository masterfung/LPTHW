states = {
	'Texas': 'TX',
	'Florida': 'FL',
	'Rhode Island': 'RI',
	'New York': 'NY',
	'California': 'CA',
	'Illinois': 'IL',
	'Oregon': 'OR'
	}

cities = {
	'IL': 'Chicago',
	'CA': 'San Francisco',
	'NY': 'New York',
	'RI': 'Providence',
	'FL': 'Orlando',
	'TX': 'Austin'
}

cities['OR'] = 'Portland'

print '*' * 10
print 'A capital of Texas is', cities['TX']
print 'A great city of Illinois is', cities['IL']

print '*' * 10
print 'The state abbreviation for Texas is', states['Texas']

print '*' * 10
for state, abbrev in states.items():
	print '{} state is abbrevated {} and has city {}'.format(state, abbrev, cities[abbrev])