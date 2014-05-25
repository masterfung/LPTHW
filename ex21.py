import math

def addition(a,b):
	return a+b

def substraction(a,b):
	return a-b

def multiplication(a,b):
	return a*b

def division(a,b):
	return a/b

age = addition(22, 13)
zipcode = substraction(90123, 12010)
mass = multiplication(123, 1230123)
iq = division(212, 2)

print 'At this {} zipcode, the average age is: {} and the mass of this city is: {} kg, and average IQ of: {}.'.format(zipcode, age, mass, iq)