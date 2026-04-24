from observers.NotificationObservable import NotificationObservable
from NotificationStrategy import NotificationStrategy
from typing import List

class NotificationEnginer(NotificationObservable):
    notification_strategies: List[NotificationStrategy] = []    
    def __init__(self, notification_observable: NotificationObservable):
        self.__notification_observable = notification_observable

    def get_notification_observable(self):
        return self.__notification_observable
    

    def add_notification_strategies(self, strategy: NotificationStrategy):
        self.notification_strategies.append(strategy)

    def remove_notification_strategy(self, strategy: NotificationStrategy):
        self.notification_strategies.remove(strategy)

    def update(self):
        notification_content = self.get_notification_observable().get_notification_content()

        for n_s in self.notification_strategies:
            n_s.send_notification(notification_content)

