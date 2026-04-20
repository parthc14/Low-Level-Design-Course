from models.Restaurant import Restaurant
from models.MenuItem import MenuItem
from typing import List


class Cart:
    cart_id_counter = 1

    def __init__(self):
        self.__cart_id = Cart.cart_id_counter
        Cart.cart_id_counter += 1
        self.__restaurant: Restaurant = None
        self.__menu_items: List[MenuItem] = []

    def get_cart_id(self):
        return self.__cart_id

    def get_restaurant(self):
        return self.__restaurant

    def set_restaurant(self, new_restaurant: Restaurant):
        self.__restaurant = new_restaurant

    def get_items(self):
        return self.__menu_items

    def add_to_cart(self, new_menu_item: MenuItem):
        if self.__restaurant is None:
            print("Cart: Cannot add item without restaurant!")
            return
        self.__menu_items.append(new_menu_item)

    def calculate_cart_total(self):
        return sum(it.get_price() for it in self.__menu_items)

    @property
    def restaurant(self):
        return self.__restaurant

    @property
    def item(self):
        return self.__menu_items
