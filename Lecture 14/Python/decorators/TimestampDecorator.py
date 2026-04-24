from NotificationDecorator import INotificationDecorator
from models.Notifications import INotification

class TimestampDecorator(INotificationDecorator):
    def __init__(self, notification: INotification):
        super().__init__(notification)
    
    def get_content(self):
        return f"[2025-04-13 14:22:00] {self.get_notification().get_content()}"