from models.Song import Song
from device.IAudioOutputDevice import IAudioOutputDevice
from typing import Optional

class AudioEngine:
    def __init__(self):
        self.__current_song: Optional[Song] = None
        self.__is_song_paused: bool = False
    

    def get_current_song_title(self):
        if self.__current_song:
            return self.__current_song.get_title()
    
    def is_paused(self):
        return self.__is_song_paused
    
    def play(self, aod: IAudioOutputDevice, song: Song):
        if self.__current_song is None:
            return RuntimeError("Cannot play a null song")

        if self.__is_song_paused and self.__current_song == song:
            self.__is_song_paused = False
            print(f"Resuming song: {song.get_title()}")
            aod.play_audio(song)
            return
        
        self.__current_song = song
        self.__is_song_paused = False
        print(f"Playing song: {song.get_title()}")
        aod.play_audio(song)

    def pause(self):
        if self.__current_song is None:
            return RuntimeError("No song is currently playing to pause.")
        if self.__is_song_paused:
            return RuntimeError("Song is already paused")
        self.__is_song_paused = True
        print(f"Pausing song: {self.__current_song.get_title()}")