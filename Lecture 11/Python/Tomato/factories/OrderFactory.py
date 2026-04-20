from abc import ABC, abstractmethod
from models.Cart import Cart
from models.User import User
from strategies.PaymentStrategy import PaymentStrategy


class OrderFactory(ABC):
    @abstractmethod
    def create_order(self, cart: Cart, user: User, payment_strategy: PaymentStrategy):
        pass
