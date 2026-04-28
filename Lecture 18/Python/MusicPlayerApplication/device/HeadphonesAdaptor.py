from IAudioOutputDevice import IAudioOutputDevice
from models.Song import Song
from external.HeadphonesAPI import HeadphoneAPI

class HeadphonesAdaptor(IAudioOutputDevice):
    def __init__(self, headphones: HeadphoneAPI):
        self.__headphones = headphones

    def get_headphones_api(self):
        return self.__headphones

    def play_audio(self, song: Song):
        payload = f"{song.get_title()} by {song.get_artist()}"
        self.get_headphones_api().play_sound_via_headphones(payload)
        
        