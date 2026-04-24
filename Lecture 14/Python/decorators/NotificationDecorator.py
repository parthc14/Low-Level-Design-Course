from abc import ABC, abstractmethod
from models.Notifications import INotification

class INotificationDecorator(INotification):
    def __init__(self, notification: INotification):
        self.__notification = notification

    def get_notification(self):
        return self.__notification
