from IAudioOutputDevice import IAudioOutputDevice
from models.Song import Song
from external.BluetoothSpeakerAPI import BluetoothSpeakerAPI

class BluetoothSpeakerAdaptor(IAudioOutputDevice):
    def __init__(self, bluetoothAPI: BluetoothSpeakerAPI):
        self.__bluetooth = bluetoothAPI

    def get_bluetooth_api(self):
        return self.__bluetooth

    def play_audio(self, song: Song):
        payload = f"{song.get_title()} by {song.get_artist()}"
        self.get_bluetooth_api().play_sound_via_bluetooth(payload)
        
        