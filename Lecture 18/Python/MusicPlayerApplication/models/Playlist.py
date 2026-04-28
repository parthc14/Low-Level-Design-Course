from typing import List
from Song import Song

class Playlist:

    def __init__(self, name: str):
        self.__play_list_name = name
        self.__song_list:  List[Song] = []

    def get_playlist_name(self):
        return self.__play_list_name

    def get_songslist(self):
        return self.__song_list
    
    @classmethod
    def get_number_of_songs(self):
        return len(self.get_songslist())
    

    def add_song_to_playlist(self, song: Song):
        if song is None:
            return RuntimeError("Cannot add null song to playlist")
        self.get_songslist().append(song)