from os import listdir
from os.path import join
from playlist import Playlist
from song import Song
from mutagen.mp3 import MP3
from mutagen.easyid3 import EasyID3


class MusicCrawler():

    def __init__(self, directory):
        self.directory = directory

    def generate_playlist(self, directory):

        files = listdir(directory)
        print (files)

        generated_playlist = Playlist("Generated")
        for name in files:

            if name[-4:] == ".mp3":
                adress = directory + "/" + name

                audio = MP3(adress, ID3=EasyID3)
                print(name)
                print(dir(audio))
                print(audio.get("title"))

                song = Song(audio.get("title"), audio.get("artist"), audio.get("album"), audio.get("rating"), audio.get("length"), audio.get("bitrate"))
                generated_playlist.songs.append(song)
        return generated_playlist


my_cralwer = MusicCrawler("/media/rolev/02AA2EBCAA2EAC5B/My Passport/Music")
print(my_cralwer.generate_playlist("/media/rolev/02AA2EBCAA2EAC5B/My Passport/Music").save("GENERATED_LIST"))


"""list = listdir("/media/rolev/02AA2EBCAA2EAC5B/My Passport/Music")
print (("\n").join(list))"""
