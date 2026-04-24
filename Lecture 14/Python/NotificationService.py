from observers.NotificationObservable import NotificationObservable
from models.Notifications import INotification
from typing import List

class NotificationService:
    observable: NotificationObservable = None
    __instance: NotificationService = None
    notifications: List[INotification] = []

    def __new__(cls):
        if cls.observable is None:
            cls.observable = super().__new__(cls)
        return cls.observable

    @staticmethod
    def get_instance():
        if NotificationService.__instance is None:
            NotificationService.__instance = NotificationService()
        return NotificationService.__instance
    
    def get_observable(self):
        return self.observable
    
    def send_notification(self, notification: INotification):
        self.notifications.append(notification)
        self.observable.set_notification(notification)
