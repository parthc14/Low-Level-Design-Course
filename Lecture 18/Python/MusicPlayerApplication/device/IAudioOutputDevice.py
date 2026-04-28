from abc import ABC, abstractmethod
from models.Song import Song

class IAudioOutputDevice(ABC):
    @abstractmethod
    def play_audio(self, song: Song):
        pass