from graph import DirectedGraph
import json
import requests


TOKEN = ('afed76ce473b13df236e4db93d50fcdf43a3abd7', '')
#r = requests.get('https://api.github.com/users/skdls-/followers', auth=TOKEN)
# print(r.json())


class GithubGraph():

    def __init__(self, name):

        self.name = name
        self.edges = {}

    def get_following(self):

        r = requests.get('https://api.github.com/users/skdls-/following', auth=TOKEN)
        array = r.json()
        #print(array)
        list_of_following = []
        for key in array:
            list_of_following.append(key['login'])
        return list_of_following

    def is_following(self, username):

        if username in self.get_following():
            return True
        return False



my_proba = GithubGraph("Proba")
print(my_proba.is_following("kal0ian"))
