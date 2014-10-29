class Song(object):

	MAX_RATING = 5
	MIN_RATING = 0
	def __init__(self, title, artist, album, rating, length, bitrate):

		self.title = title
		self.artist = artist
		self.album = album
		self.rating = rating
		self.length = length
		self.bitrate = bitrate

	def rate(self, value):
		if int(value) <= self.MAX_RATING and int(value) >= self.MIN_RATING:
			self.rating = int(value)
		else:
			raise ValueError

if __name__ == '__main__':
	main()