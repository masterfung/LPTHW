def holyHappiness(oneBlessing, twoBlessing, amount):
	print 'I know you have great things to do in this \
world but you can always enjoy my first gift of %s.' % \
	oneBlessing
	print 'However, I need to present you with one more \
	gift. And this gift is: %s.' % twoBlessing
	print 'The total amount of supply you will be receiving \
is %d days worth. \n' % (amount * 6)

print holyHappiness('cookies', 'water', 30)

print 'With the power of multiplication, the new worth:'
print holyHappiness('cookies', 'water', 30*50)

def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket.\n"


print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)


print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)