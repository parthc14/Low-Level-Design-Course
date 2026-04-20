from models.Order import Order

class PickupOrder(Order):
    def __init__(self, restaurant, user, payment_method, items, scheduled_time=None):
        super().__init__(restaurant, user, payment_method, items, scheduled_time)

    def get_type(self):
        return "Pickup"
