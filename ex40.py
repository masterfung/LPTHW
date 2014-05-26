class Song(object):
	def __init__(self, lyrics):
		self.lyrics = lyrics
	def sing(self):
		for line in self.lyrics:
			print line

happy_bday = Song(["Happy birthday to you",
					"We wish a joyous time",
					"So I'll stop right there"])

good_jam = Song(['Many nights we prayed',
				'With no proof, anyone could hear',
				'In our heart, a hopeful song'])

super_jam = ['Clap your hands if you feel',
			'happiness is the truth',
			'cause I\'m happy, happy, happy']

happy_bday.sing()

good_jam.sing()


Song(super_jam).sing()