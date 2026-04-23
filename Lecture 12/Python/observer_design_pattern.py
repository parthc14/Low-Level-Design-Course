from abc import ABC, abstractmethod
from typing import List

class ISubscriber(ABC):
    def __init__(self, name: str):
        self.__name = name

    def get_subscriber_name(self):
        return self.__name
    
    @abstractmethod
    def update(self):
        pass

class IChannel(ABC):
    @abstractmethod
    def subscribe(self, subscriber: ISubscriber):
        pass

    @abstractmethod
    def un_subscribe(self, subscriber: ISubscriber):
        pass

    @abstractmethod
    def notify_subsribers(self):
        pass


class Channel(IChannel):
    subsribers: List[ISubscriber] = []
    lastest_video: str = ''

    def __init__(self, name: str):
        self.__name = name
    
    def get_name(self):
        return self.__name
    
    def subscribe(self, subscriber):
       if subscriber not in self.subsribers:
           self.subsribers.append(subscriber)
           print(f"{subscriber} subscribed to {self.get_name()}")
    
    def un_subscribe(self, subscriber):
        exists = subscriber in self.subsribers
        if exists:
            self.subsribers.remove(subscriber)
            print(f"{subscriber.get_subscriber_name()} un_subscribed to {self.get_name()}")
    
    def notify_subsribers(self):
        for sub in self.subsribers:
            sub.update()

    def upload_video(self, title: str):
        self.lastest_video = title
        print(f"{self.get_name()} uploaded {title}")
        self.notify_subsribers()

    def get_video_data(self):
        print(f"Checkout our new video: {self.lastest_video}")

class Subscriber(ISubscriber):
    def __init__(self, channel: Channel, name: str):
        self.__channel = channel
        super().__init__(name)

    def get_channel(self):
        return self.__channel


    def update(self):
        print(f"hey {self.get_subscriber_name()}, {self.get_channel().get_name()} uploaded a video!")
    
if __name__ == "__main__":
    channel = Channel("CoderArmy")

    subs1 = Subscriber(channel, "Parth")
    subs2 = Subscriber(channel, "Surbhi")

    channel.subscribe(subs1)
    channel.subscribe(subs2)

    channel.upload_video("New video on LLD")

    channel.get_video_data()
    
    channel.un_subscribe(subs2)

    channel.upload_video("Another video on LLD")
    channel.get_video_data()


