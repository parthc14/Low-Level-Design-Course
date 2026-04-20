from models.Order import Order

class DeliveryOrder(Order):
    def __init__(self, restaurant, user, payment_method, items, scheduled_time=None, user_address=""):
        super().__init__(restaurant, user, payment_method, items, scheduled_time)
        self.__user_address = user_address

    def get_type(self):
        return "Delivery"

    def get_address(self):
        return self.__user_address

    def set_address(self, new_address):
        self.__user_address = new_address
