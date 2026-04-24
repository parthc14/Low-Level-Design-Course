from Notifications import INotification

class SimpleNotification(INotification):
    def __init__(self, text: str):
        self.__text = text

    def get_content(self):
        return self.__text

