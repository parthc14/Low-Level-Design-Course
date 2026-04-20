from models.Restaurant import Restaurant
from typing import List


class RestaurantManager:
    __instance = None

    def __init__(self):
        self.__restaurants: List[Restaurant] = []

    @staticmethod
    def get_instance():
        if RestaurantManager.__instance is None:
            RestaurantManager.__instance = RestaurantManager()
        return RestaurantManager.__instance

    def get_restaurants(self) -> List[Restaurant]:
        return self.__restaurants

    def add_restaurant(self, restaurant: Restaurant):
        self.__restaurants.append(restaurant)

    def search_by_location(self, location: str) -> List[Restaurant]:
        location = location.lower()
        results = []
        for r in self.__restaurants:
            if r.get_address().lower() == location:
                results.append(r)
        return results
