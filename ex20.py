from sys import argv

script, input = argv

def printAll(file):
	print file.read()

def rewind(f):
	f.seek(0)

def printSingleLine(eachLine, file):
	print eachLine, file.readline()

currentFile = open(input)

print 'First let us print the whole file:\n'

printAll(currentFile)

print 'Let us witness the power of rewind!'

rewind(currentFile)

print 'We are going to reprint the three lines.'

currentLine = 1
printSingleLine(currentLine, currentFile)

currentLine += 1
printSingleLine(currentLine, currentFile)

currentLine += 1
printSingleLine(currentLine, currentFile)
