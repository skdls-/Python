import unittest
from song import Song

class TestSong(unittest.TestCase):

	def setUp(self):
		self.song = Song("Title", "Artist","Album", 5.0, 4.22, 320)

	def test_init(self):
		self.assertEqual(self.song.title, "Title")
		self.assertEqual(self.song.artist, "Artist")
		self.assertEqual(self.song.album, "Album")
		self.assertEqual(self.song.rating, 5.0)
		self.assertEqual(self.song.length, 4.22)
		self.assertEqual(self.song.bitrate, 320)

	def test_rate(self):
		self.song.rate(4)
		self.assertEqual(self.song.rating, 4)
		with self.assertRaises(ValueError):
			self.song.rate(6)


if __name__ == '__main__':
	unittest.main()