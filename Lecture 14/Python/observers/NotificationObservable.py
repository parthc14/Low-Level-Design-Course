from Observable import IObservable
from Observer import IObserver
from models.Notifications import INotification
from typing import List

class NotificationObservable(IObservable):
    observers: List[IObserver] = []
    def __init__(self, notification: INotification):
        self.__current_notification = notification

    def get_current_notification(self):
        return self.__current_notification
    
    def add_observer(self, observer: IObserver):
        if observer not in self.observers:
            self.observers.append(observer)
    
    def remove_observer(self, observer: IObserver):
        if observer in self.observers:
            self.observers.remove(observer)
    
    def notify_observer(self):
        for observer in self.observers:
            observer.update()
    
    def get_notification_content(self):
        return self.get_current_notification().get_content()
    
    def set_notification(self, notification: INotification):
        if self.get_current_notification():
            self.get_current_notification() = None
        self.get_current_notification = notification
        self.notify_observer()
