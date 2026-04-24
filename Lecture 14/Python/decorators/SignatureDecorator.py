from NotificationDecorator import INotificationDecorator
from models.Notifications import INotification

class SignatureDecorator(INotificationDecorator):
    def __init__(self, notification: INotification, signature: str):
        super().__init__(notification)
        self.__signature = signature
    
    def get_signature(self):
        return self.__signature

    def get_content(self):
        return f"{self.get_notification().get_content()} \n--- {self.get_signature()}"