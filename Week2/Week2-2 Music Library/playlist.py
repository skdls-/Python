import json
from song import Song


class Playlist:

    def __init__(self, name):

        self.songs = []
        self.name = name

    def add_song(self, song):

        self.songs.append(song)

    def remove_song(self, songname):

        buff = []
        for song in self.songs:
            if song.title != songname:
                buff.append(song)
        self.songs = buff

    def total_lenght(self):

        sum = 0
        for song in self.songs:
            sum += song.length
        return sum

    def remove_disrated(self, rating):

        buff = []
        for song in self.songs:
            if song.rating >= rating:
                buff.append(song)
        self.songs = buff

    def remove_bad_quality(self, quality):

        buff = []
        for song in self.songs:
            if song.bitrate >= quality:
                buff.append(song)
        self.songs = buff

    def show_artits(self):

        buff = []
        for song in self.songs:
            if song.artist not in buff:
                buff.append(song.artist)
        buff.sort()
        return buff

    """def __str__(self):

        my_str = ""
        for song in self.songs:
            if song.length < 60:
                mins = 0
                secs = song.length
            else:
                mins = song.length // 60
                secs = song.length % mins
            info = '{} {} - {}:{}\n'.format(song.artist,
                                            song.title, mins, secs)
            my_str += info
        return my_str"""

    def save(self, filename):
        #"name": filename
        dict = {"name": filename, "songs": []}
        for song in self.songs:
            dict["songs"].append(song.__dict__)
        file = open(filename, "w")
        json_text = json.dumps(dict, indent=4, separators=(',', ': '))
        file.write(json_text)

        # file.close()

    """def load(self, filename):
        file = open(filename, "r")
        file.read()
        json.loads(file)
        current_playlist = Playlist(file.songs, file.name) """

    def load(self, filename):
        with open(filename, 'r') as load_file:
            load_data = json.load(load_file)
            loaded_playlist = Playlist(load_data['name'])
            for song_data in load_data['songs']:
                song = Song(song_data['title'], song_data['artist'], song_data['album'], song_data['rating'], song_data['length'], song_data['bitrate'])
                loaded_playlist.add_song(song)
            return loaded_playlist


        """test_song = Song("dsdas", "asdasd", 'dasds', 34 , 5 ,4)

    song_dict = {}
    song_dict['title'] = test_song.title

    print(test_song.__dict__) 
song1 = Song("Title1", "Artist", "Album", 5.0, 4, 320)
song2 = Song("Title2", "Artist", "Album", 2.0, 2, 320)
song3 = Song("Title3", "Artist2", "Album", 5.0, 4, 128)
my_playlist = Playlist("Playlist")
my_playlist.songs.append(song1)
my_playlist.songs.append(song2)
my_playlist.songs.append(song3)
str(my_playlist.load('playlist1') """
