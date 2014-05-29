#code optimized!! :)
class Animal(object):
	num_of_legs = 0
	def __init__(self, name, color, count, height):
		self._name = name
		self._color = color
		self._count = count
		self._height = height
	def count_legs(self):
		print 'Your pet, %s, has %s of legs.' % (self._name, self._count)
	def features(self):
		print 'This pet has the natural color of %s and is about this tall: %d cm.' % (self._color, self._height)

class Dog(Animal):
	def bark(self):
		print 'Woof!'

zeb = Animal('Zeb', 'red', 4, 39)
zeb.features()
zeb.count_legs()


# happle = Animal('Happle')
# happle.features('red', 62)

class Person(object):
	def __init__(self, name):
		self._name = name

class Employee(Person):
	def __init__(self, name, salary):
		super(Employee,self).__init__(name) #need to delve into this
		self.salary = salary
		print '%s is making %d per year!' % (name, salary)

#trying out some good examples
joe = Employee('Joe', 120000)
harry = Employee('Harry', 1290000)
robot = Employee('The Robot', 5000)
erica = Employee('Erica', 100200000)