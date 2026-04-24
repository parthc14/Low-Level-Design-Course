from NotificationStrategy import NotificationStrategy

class EmailNotification(NotificationStrategy):
    def __init__(self, email_id: str):
        self.__email = email_id

    def get_email_id(self):
        return self.__email
    
    def send_notification(self, content: str):
        print(f"Sending email notifications to {self.get_email_id()} with content: {content}")