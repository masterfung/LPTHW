class Animal(object):
	num_of_legs = 0
	def __init__(self, name):
		self._name = name
	def count_legs(self, count):
		self._count = count
		print 'Your pet has %s of legs.' % count

class Dog(Animal):
	def bark(self):
		print 'Woof!'

zeb = Animal('Zeb')
zeb.count_legs(4)

class Person(object):
	def __init__(self, name):
		self._name = name

class Employee(Person):
	def __init__(self, name, salary):
		super(Employee,self).__init__(name) #need to delve into this
		self.salary = salary
		print '%s is making %d per year!' % (name, salary)

joe = Employee('Joe', 120000)
harry = Employee('Harry', 1290000)
erica = Employee('Erica', 100200000)