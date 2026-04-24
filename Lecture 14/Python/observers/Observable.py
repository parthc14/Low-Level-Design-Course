from abc import ABC, abstractmethod

class IObservable(ABC):
    @abstractmethod
    def add_observer(self):
        pass

    @abstractmethod
    def remove_observer(self):
        pass

    @abstractmethod
    def notify_observer(self):
        pass