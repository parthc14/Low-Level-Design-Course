from abc import ABC, abstractmethod
from datetime import datetime
from typing import List, Optional

# ============================
#      Notification & Decorators
# ============================

class INotification(ABC):
    @abstractmethod
    def get_content(self) -> str:
        pass

# Concrete Notification
class SimpleNotification(INotification):
    def __init__(self, msg: str):
        self._text = msg

    def get_content(self) -> str:
        return self._text

# Abstract Decorator
class INotificationDecorator(INotification):
    def __init__(self, n: INotification):
        self._notification = n

# Decorators
class TimestampDecorator(INotificationDecorator):
    def get_content(self) -> str:
        # Static timestamp to match your Java example, though datetime.now() is more practical
        return f"[2025-04-13 14:22:00] {self._notification.get_content()}"

class SignatureDecorator(INotificationDecorator):
    def __init__(self, n: INotification, sig: str):
        super().__init__(n)
        self._signature = sig

    def get_content(self) -> str:
        return f"{self._notification.get_content()}\n-- {self._signature}\n\n"


# ============================
#  Observer Pattern Components
# ============================

class IObserver(ABC):
    @abstractmethod
    def update(self):
        pass

class IObservable(ABC):
    @abstractmethod
    def add_observer(self, observer: IObserver):
        pass

    @abstractmethod
    def remove_observer(self, observer: IObserver):
        pass

    @abstractmethod
    def notify_observers(self):
        pass

class NotificationObservable(IObservable):
    def __init__(self):
        self._observers: List[IObserver] = []
        self._current_notification: Optional[INotification] = None

    def add_observer(self, obs: IObserver):
        self._observers.append(obs)

    def remove_observer(self, obs: IObserver):
        self._observers.remove(obs)

    def notify_observers(self):
        for obs in self._observers:
            obs.update()

    def set_notification(self, notification: INotification):
        self._current_notification = notification
        self.notify_observers()

    def get_notification_content(self) -> str:
        return self._current_notification.get_content() if self._current_notification else ""


# ============================
#       NotificationService (Singleton)
# ============================

class NotificationService:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(NotificationService, cls).__new__(cls)
            cls._instance._observable = NotificationObservable()
            cls._instance._notifications = []
        return cls._instance

    @classmethod
    def get_instance(cls):
        return cls()

    def get_observable(self) -> NotificationObservable:
        return self._observable

    def send_notification(self, notification: INotification):
        self._notifications.append(notification)
        self._observable.set_notification(notification)


# ============================
#       Concrete Observers
# ============================

class Logger(IObserver):
    def __init__(self, observable: Optional[NotificationObservable] = None):
        # If no observable provided, use the Singleton instance (as per your updated Java code)
        self._notification_observable = observable or NotificationService.get_instance().get_observable()
        self._notification_observable.add_observer(self)

    def update(self):
        print(f"Logging New Notification : \n{self._notification_observable.get_notification_content()}")


# ============================
#  Strategy Pattern Components
# ============================

class INotificationStrategy(ABC):
    @abstractmethod
    def send_notification(self, content: str):
        pass

class EmailStrategy(INotificationStrategy):
    def __init__(self, email_id: str):
        self._email_id = email_id

    def send_notification(self, content: str):
        print(f"Sending email Notification to: {self._email_id}\n{content}")

class SMSStrategy(INotificationStrategy):
    def __init__(self, mobile_number: str):
        self._mobile_number = mobile_number

    def send_notification(self, content: str):
        print(f"Sending SMS Notification to: {self._mobile_number}\n{content}")

class PopUpStrategy(INotificationStrategy):
    def send_notification(self, content: str):
        print(f"Sending Popup Notification: \n{content}")

class NotificationEngine(IObserver):
    def __init__(self, observable: Optional[NotificationObservable] = None):
        self._notification_observable = observable or NotificationService.get_instance().get_observable()
        self._notification_observable.add_observer(self)
        self._strategies: List[INotificationStrategy] = []

    def add_notification_strategy(self, ns: INotificationStrategy):
        self._strategies.append(ns)

    def update(self):
        content = self._notification_observable.get_notification_content()
        for strategy in self._strategies:
            strategy.send_notification(content)


# ============================
#          Main Logic
# ============================

if __name__ == "__main__":
    # Access Singleton Service
    notification_service = NotificationService.get_instance()

    # Create Observers (they auto-attach to the Singleton's observable)
    logger = Logger()
    notification_engine = NotificationEngine()

    # Configure Strategies
    notification_engine.add_notification_strategy(EmailStrategy("random.person@gmail.com"))
    notification_engine.add_notification_strategy(SMSStrategy("+91 9876543210"))
    notification_engine.add_notification_strategy(PopUpStrategy())

    # Build Decorated Notification
    notif = SimpleNotification("Your order has been shipped!")
    notif = TimestampDecorator(notif)
    notif = SignatureDecorator(notif, "Customer Care")

    # Dispatch
    notification_service.send_notification(notif)