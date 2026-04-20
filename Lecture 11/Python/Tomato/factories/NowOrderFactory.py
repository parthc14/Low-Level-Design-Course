from factories.OrderFactory import OrderFactory
from models.DeliveryOrder import DeliveryOrder

class NowOrderFactory(OrderFactory):
    def create_order(self, cart, user, payment_strategy):
        order = DeliveryOrder(cart.restaurant, user, payment_strategy, cart.item, "Now")
        return order
