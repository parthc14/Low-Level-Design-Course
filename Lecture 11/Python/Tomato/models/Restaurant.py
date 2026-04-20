from models.MenuItem import MenuItem
from typing import List


class Restaurant:
    restaurant_id = 1

    def __init__(self, name: str, address: str):
        self._restaurant_id = Restaurant.restaurant_id
        Restaurant.restaurant_id += 1
        self.__name = name
        self.__address = address
        self.__menu_items: List[MenuItem] = []

    def get_name(self) -> str:
        return self.__name

    def set_name(self, new_name: str):
        self.__name = new_name

    def get_address(self) -> str:
        return self.__address

    def set_address(self, new_address: str):
        self.__address = new_address

    def get_menu_items(self) -> List[MenuItem]:
        return self.__menu_items

    def add_menu_item(self, item: MenuItem):
        self.__menu_items.append(item)

    @property
    def address(self):
        return self.__address

    @property
    def name(self):
        return self.__name

    @property
    def items(self):
        return self.__menu_items
