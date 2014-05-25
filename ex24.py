print 'Everything is awesome!'

song = '''
We clawed, we chained
our hands, and just never asking
why
Dont you ever say, I just walked away
I will always love you. I can't live a life
running from my life, I will always love you.
'''

print song

def magical(substance):
	unicorns = substance * 800
	cheetos = substance / 20
	fairies = substance *80 ** 2
	return unicorns, cheetos, fairies


start = 2000
unicorns, cheetos, fairies = magical(start)

print 'This is where the magic number will start %d. Rdy?' % \
start 
print 'We have %d unicorns, %d cheetos, and %d fairies in this\
story.' % (unicorns, cheetos, fairies)