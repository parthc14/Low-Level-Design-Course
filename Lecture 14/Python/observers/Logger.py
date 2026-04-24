from Observer import IObserver
from NotificationObservable import NotificationObservable

class Logger(IObserver):
    def __init__(self, notification_observable: NotificationObservable):
        self.__notification_observable = notification_observable
    
    def get_notification_observable(self):
        return self.__notification_observable


    def update(self):
        print(f"Logging new notification: {self.get_notification_observable().get_notification_content()}")