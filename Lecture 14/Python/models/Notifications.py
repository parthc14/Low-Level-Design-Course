from abc import ABC, abstractmethod


class INotification(ABC):
    @abstractmethod
    def get_content(self):
        pass

