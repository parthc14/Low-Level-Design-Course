from typing import List
from models.Order import Order


class OrderManager:
    def __init__(self):
        self.__orders: List[Order] = []

    def get_orders(self) -> List[Order]:
        return self.__orders

    def place_order(self, order: Order):
        self.__orders.append(order)
