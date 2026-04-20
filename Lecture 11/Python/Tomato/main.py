from TomatoApp import TomatoApp
from models.User import User
from strategies.UPIStrategy import UPIStrategy
from strategies.CreditCardStrategy import CreditCardStrategy
from factories.NowOrderFactory import NowOrderFactory
from models.PickupOrder import PickupOrder

def test_complete_e2e_workflow():
    """Complete end-to-end workflow simulation"""
    print("=" * 60)
    print("TOMATO APP - COMPLETE E2E WORKFLOW TEST")
    print("=" * 60)

    # 1. Initialize app
    tomato = TomatoApp()

    # 2. Create user
    user = User(101, "Parth", "Chitroda")
    print(f"\n1. User Created: {user.get_name()}")

    # 3. Search restaurants
    print(f"\n2. Searching restaurants in Mumbai...")
    restaurants = tomato.search_restaurants("Mumbai")
    if not restaurants:
        print("No restaurants found!")
        return

    print(f"   Found {len(restaurants)} restaurant(s):")
    for r in restaurants:
        print(f"   - {r.get_name()}")

    # 4. Select restaurant
    selected_restaurant = restaurants[0]
    tomato.select_restaurant(user, selected_restaurant)
    print(f"\n3. Selected Restaurant: {selected_restaurant.get_name()}")

    # 5. Browse menu and add items to cart
    cart = user.get_cart()
    menu_items = selected_restaurant.get_menu_items()
    print(f"\n4. Adding items to cart:")
    cart.add_to_cart(menu_items[0])
    print(f"   + {menu_items[0].get_name()} - ₹{menu_items[0].get_price()}")
    cart.add_to_cart(menu_items[1])
    print(f"   + {menu_items[1].get_name()} - ₹{menu_items[1].get_price()}")

    # 6. Calculate total
    total = cart.calculate_cart_total()
    print(f"\n5. Cart Total: ₹{total}")

    # 7. Create order with payment strategy (UPI)
    payment = UPIStrategy("9876543210")
    order = PickupOrder(selected_restaurant, user, payment, cart.get_items())
    print(f"\n6. Order Created (Pickup)")
    print(f"   Order ID: {order.get_order_id()}")
    print(f"   Type: {order.get_type()}")
    print(f"   Items: {len(order.get_items())}")

    # 8. Process payment
    print(f"\n7. Processing Payment...")
    if order.process_payment():
        print(f"   ✓ Payment successful for ₹{total}")

    # 9. Place order
    order_manager = tomato.get_order_manager()
    order_manager.place_order(order)
    print(f"\n8. Order Placed Successfully!")
    print(f"   Order #{order.get_order_id()} is confirmed")

    # 10. Show all orders
    all_orders = order_manager.get_orders()
    print(f"\n9. Total Orders in System: {len(all_orders)}")

    print("\n" + "=" * 60)
    print("E2E WORKFLOW COMPLETED SUCCESSFULLY")
    print("=" * 60)

def test_delivery_order_workflow():
    """Test delivery order workflow"""
    print("\n\n" + "=" * 60)
    print("DELIVERY ORDER WORKFLOW TEST")
    print("=" * 60)

    tomato = TomatoApp()
    user2 = User(102, "John", "Doe")
    print(f"\n1. User Created: {user2.get_name()}")

    restaurants = tomato.search_restaurants("Delhi")
    print(f"2. Found {len(restaurants)} restaurants in Delhi")

    tomato.select_restaurant(user2, restaurants[0])
    restaurant = restaurants[0]
    print(f"3. Selected: {restaurant.get_name()}")

    cart = user2.get_cart()
    menu = restaurant.get_menu_items()
    for item in menu[:2]:
        cart.add_to_cart(item)

    print(f"4. Added {len(cart.get_items())} items to cart")
    print(f"   Total: ₹{cart.calculate_cart_total()}")

    from models.DeliveryOrder import DeliveryOrder
    payment = CreditCardStrategy("1234-5678-9012-3456")
    delivery_order = DeliveryOrder(restaurant, user2, payment, cart.get_items(), "Now", "123 Main St, Delhi")
    print(f"\n5. Created Delivery Order")
    print(f"   Order ID: {delivery_order.get_order_id()}")
    print(f"   Delivery Address: {delivery_order.get_address()}")

    print(f"\n6. Processing Payment (Credit Card)...")
    if delivery_order.process_payment():
        print(f"   ✓ Payment successful for ₹{cart.calculate_cart_total()}")

    tomato.get_order_manager().place_order(delivery_order)
    print(f"\n7. Delivery Order #{delivery_order.get_order_id()} Placed!")

    print("\n" + "=" * 60)

if __name__ == "__main__":
    test_complete_e2e_workflow()
    test_delivery_order_workflow()
