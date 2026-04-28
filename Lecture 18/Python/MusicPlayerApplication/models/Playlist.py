from typing import List
from Song import Song

class Playlist:
    song_list: List[Song] = []

    def __init__(self, name: str):
        self.__play_list_name = name

    def get_playlist_name(self):
        return self.__play_list_name
    
    @classmethod
    def get_songslist():
        return Playlist.song_list
    
    @classmethod
    def get_number_of_songs():
        return len(Playlist.song_list)
    

    def add_song_to_playlist(self, song: Song):
        if song is None:
            return RuntimeError("Cannot add null song to playlist")
        Playlist.song_list.append(song)