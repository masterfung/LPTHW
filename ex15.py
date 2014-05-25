from sys import argv

script, filename = argv

file = open(filename)

print 'here is your file, called %s: ' % filename
print file.read()

print 'type the filename again:'
fileNameAgain = raw_input('-> ')

fileAgain = open(fileNameAgain)

print fileAgain.read()