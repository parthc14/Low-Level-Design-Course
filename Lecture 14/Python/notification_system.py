from abc import ABC, abstractmethod
from datetime import datetime

# ============================
#      Notification & Decorators
# ============================

class INotification(ABC):
    @abstractmethod
    def get_content(self) -> str:
        pass

# Concrete Notification: simple text notification.
class SimpleNotification(INotification):
    def __init__(self, msg: str):
        self._text = msg

    def get_content(self) -> str:
        return self._text

# Abstract Decorator: wraps a Notification object.
class INotificationDecorator(INotification):
    def __init__(self, notification: INotification):
        self._notification = notification

# Decorator to add a timestamp to the content.
class TimestampDecorator(INotificationDecorator):
    def get_content(self) -> str:
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return f"[{now}] {self._notification.get_content()}"

# Decorator to append a signature to the content.
class SignatureDecorator(INotificationDecorator):
    def __init__(self, notification: INotification, sig: str):
        super().__init__(notification)
        self._signature = sig

    def get_content(self) -> str:
        return f"{self._notification.get_content()}\n-- {self._signature}\n"


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

# Concrete Observable
class NotificationObservable(IObservable):
    def __init__(self):
        self._observers = []
        self._current_notification = None

    def add_observer(self, obs: IObserver):
        if obs not in self._observers:
            self._observers.append(obs)

    def remove_observer(self, obs: IObserver):
        self._observers.remove(obs)

    def notify_observers(self):
        for observer in self._observers:
            observer.update()

    def set_notification(self, notification: INotification):
        self._current_notification = notification
        self.notify_observers()

    def get_notification_content(self) -> str:
        return self._current_notification.get_content() if self._current_notification else ""


# Concrete Observer 1
class Logger(IObserver):
    def __init__(self, observable: NotificationObservable):
        self._observable = observable

    def update(self):
        print(f"Logging New Notification:\n{self._observable.get_notification_content()}")


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
        print(f"Sending Popup Notification:\n{content}")

# Concrete Observer 2 using Strategies
class NotificationEngine(IObserver):
    def __init__(self, observable: NotificationObservable):
        self._observable = observable
        self._strategies = []

    def add_notification_strategy(self, ns: INotificationStrategy):
        self._strategies.append(ns)

    def update(self):
        content = self._observable.get_notification_content()
        for strategy in self._strategies:
            strategy.send_notification(content)


# ============================
#       NotificationService
# ============================

class NotificationService:
    _instance = None

    def __new__(cls):
        """Implement Singleton Pattern"""
        if cls._instance is None:
            cls._instance = super(NotificationService, cls).__new__(cls)
            cls._instance._observable = NotificationObservable()
            cls._instance._notifications = []
        return cls._instance

    @property
    def observable(self):
        return self._observable

    def send_notification(self, notification: INotification):
        self._notifications.append(notification)
        self._observable.set_notification(notification)


# ============================
#          Main Execution
# ============================

if __name__ == "__main__":
    # Singleton access
    service = NotificationService()
    obs = service.observable

    # Setup Observers
    logger = Logger(obs)
    engine = NotificationEngine(obs)

    # Setup Strategies
    engine.add_notification_strategy(EmailStrategy("random.person@gmail.com"))
    engine.add_notification_strategy(SMSStrategy("+91 9876543210"))
    engine.add_notification_strategy(PopUpStrategy())

    # Attach Observers to Observable
    obs.add_observer(logger)
    obs.add_observer(engine)

    # Create Decorated Notification
    msg = SimpleNotification("Your order has been shipped!")
    msg = TimestampDecorator(msg)
    msg = SignatureDecorator(msg, "Customer Care")

    # Fire Notification
    service.send_notification(msg)