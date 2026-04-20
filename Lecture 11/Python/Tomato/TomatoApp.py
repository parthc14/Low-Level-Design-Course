from managers.RestaurantManager import RestaurantManager
from managers.OrderManager import OrderManager
from models.Restaurant import Restaurant
from models.MenuItem import MenuItem
from models.User import User
from typing import List


class TomatoApp:
    def __init__(self):
        self.__restaurant_manager = RestaurantManager.get_instance()
        self.__order_manager = OrderManager()
        self._seed_data()

    def _seed_data(self):
        """Pre-populate with sample restaurants and menu items."""
        r1 = Restaurant("Pizza Palace", "Delhi")
        r1.add_menu_item(MenuItem(1, "Margherita Pizza", 250.0))
        r1.add_menu_item(MenuItem(2, "Pepperoni Pizza", 350.0))
        r1.add_menu_item(MenuItem(3, "Garlic Bread", 120.0))

        r2 = Restaurant("Burger Barn", "Delhi")
        r2.add_menu_item(MenuItem(4, "Classic Burger", 180.0))
        r2.add_menu_item(MenuItem(5, "Cheese Burger", 220.0))
        r2.add_menu_item(MenuItem(6, "Fries", 90.0))

        r3 = Restaurant("Sushi Spot", "Mumbai")
        r3.add_menu_item(MenuItem(7, "California Roll", 400.0))
        r3.add_menu_item(MenuItem(8, "Salmon Nigiri", 300.0))

        self.__restaurant_manager.add_restaurant(r1)
        self.__restaurant_manager.add_restaurant(r2)
        self.__restaurant_manager.add_restaurant(r3)

    def search_restaurants(self, location: str) -> List[Restaurant]:
        """Search for restaurants by location."""
        return self.__restaurant_manager.search_by_location(location)

    def select_restaurant(self, user: User, restaurant: Restaurant):
        """Set the selected restaurant on the user's cart."""
        user.get_cart().set_restaurant(restaurant)

    def get_order_manager(self) -> OrderManager:
        return self.__order_manager

    def get_restaurant_manager(self) -> RestaurantManager:
        return self.__restaurant_manager
