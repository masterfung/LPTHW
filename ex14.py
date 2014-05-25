from sys import argv

script, user_name = argv
prompt = '-****->>> '

print "Hi awesome %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few short questions."

print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where is your residence %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print 'What is your favorite city of all time?'
city = raw_input(prompt)

print """
My favorability with you is %r, and I find that response fascinating!
Your residential location is %r. That is a great place to live in :).
And you have a %r computer. Nice! I do too.
The brotherhood of computer love your response on %r being the best city of all time!
""" % (likes, lives, computer, city)