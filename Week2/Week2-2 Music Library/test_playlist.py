import unittest
from song import Song
from playlist import Playlist

class TestPlaylist(unittest.TestCase):

    def setUp(self):

        self.song1 = Song("Title1", "Artist","Album", 5.0, 4, 320)
        self.song2 = Song("Title2", "Artist","Album", 2.0, 2, 320)
        self.song3 = Song("Title3", "Artist2","Album", 5.0, 4, 128)
        self.my_playlist = Playlist("Playlist")
        self.my_playlist.songs.append(self.song1)
        self.my_playlist.songs.append(self.song2)
        self.my_playlist.songs.append(self.song3)

    def test_init(self):

        self.assertEqual(self.my_playlist.songs, [self.song1, self.song2, self.song3])
        self.assertEqual(self.my_playlist.name, "Playlist")

    def test_add_song(self):

        self.song4 = Song("Title", "Artist","Album", 5.0, 4.22, 320)
        self.my_playlist.add_song(self.song4)
        self.assertEqual(self.my_playlist.songs, [self.song1, self.song2, self.song3, self.song4])

    def test_remove_song(self):

        self.my_playlist.remove_song("Title2")
        self.assertEqual(self.my_playlist.songs, [self.song1, self.song3])

    def test_total_lenght(self):

        self.assertEqual(self.my_playlist.total_lenght(), 10)

    def test_remove_disrated(self):

        self.my_playlist.remove_disrated(3)
        self.assertEqual(self.my_playlist.songs, [self.song1, self.song3])

    def test_remove_bad_quality(self):

        self.my_playlist.remove_bad_quality(320)
        self.assertEqual(self.my_playlist.songs, [self.song1, self.song2])

    def test_show_artists(self):

        self.assertEqual(self.my_playlist.show_artits(), ["Artist", "Artist2"])

    def test_str(self):

        print(self.my_playlist.str()) 

    


if __name__ == '__main__':
    unittest.main()