from sys import argv

#organ replaces Zed's version of filename. Cryptic I know but
# who cares. I know I know...
script, organ = argv

print 'Exciting things will happen to the file %s: ' % organ

print 'We will be opening the file... please wait'
file = open(organ, 'w')

print 'The file has been opened. Next, we need to truncate'
file.truncate()

print 'Now, please enter three new lines of statements:'
first = raw_input('First line is: ')
second = raw_input('Second line is: ')
third = raw_input('Third line is: ')

print 'The systen will now commit the writing process'

file.write(first)
file.write('\n')
file.write(second)
file.write('\n')
file.write(third)

print 'Since we did everythingm, the file will now close.'
file.close()