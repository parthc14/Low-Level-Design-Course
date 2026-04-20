from abc import ABC, abstractmethod
from models.Restaurant import Restaurant
from models.User import User
from strategies.PaymentStrategy import PaymentStrategy
from models.MenuItem import MenuItem
from typing import List


class Order(ABC):
    order_id_counter = 1

    def __init__(self, restaurant: Restaurant, user: User, payment_method: PaymentStrategy,
                 items: List[MenuItem], scheduled_time: str = None):
        self.__order_id = Order.order_id_counter
        Order.order_id_counter += 1
        self.__restaurant = restaurant
        self.__user = user
        self.__payment_method = payment_method
        self.__scheduled_time = scheduled_time
        self.__items = items

    def get_order_id(self):
        return self.__order_id

    def get_payment_method(self):
        return self.__payment_method

    def get_items(self):
        return self.__items

    def process_payment(self):
        if self.__payment_method is not None:
            self.__payment_method.pay(sum(it.get_price() for it in self.__items))
            return True
        print("Order: Payment method not set")
        return False

    @abstractmethod
    def get_type(self):
        pass

    @property
    def payment_method(self):
        return self.__payment_method

    @property
    def items(self):
        return self.__items

    @property
    def order_id(self):
        return self.__order_id
