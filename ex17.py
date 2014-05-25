from sys import argv
from os.path import exists

script, coming, going = argv

print 'Copying from %s and going to %s.' % (coming, going)

substance = open(coming)
inside = substance.read()

print 'The input file is %d bytes long' % len(inside)

print 'Does the output file eist? %r' % exists(going)
print 'Ready, hit RETURN to continue or Ctrl+C to abort.'
raw_input() #monitors for input!

betterSubstance = open(going, 'w')
betterSubstance.write(inside)

print 'Your request has been finished'

betterSubstance.close()
substance.close()