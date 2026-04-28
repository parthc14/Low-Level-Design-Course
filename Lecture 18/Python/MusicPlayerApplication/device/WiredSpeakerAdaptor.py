from IAudioOutputDevice import IAudioOutputDevice
from models.Song import Song
from external.WiredSpeakerAPI import WiredSpeakerAPI

class WiredSpeakerAdaptor(IAudioOutputDevice):
    def __init__(self, wired_speaker: WiredSpeakerAPI):
        self.__wired_speaker = wired_speaker

    def get_wired_speaker_api(self):
        return self.__wired_speaker

    def play_audio(self, song: Song):
        payload = f"{song.get_title()} by {song.get_artist()}"
        self.get_wired_speaker_api().play_sound_via_wired_speaker(payload)
        
        