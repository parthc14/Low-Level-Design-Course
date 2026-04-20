from models.Cart import Cart

class User:
    def __init__(self, user_id: int, name: str, address: str):
        self.__user_id = user_id
        self.__name = name
        self.__address = address
        self.__cart: Cart = Cart()

    def get_user_id(self) -> int:
        return self.__user_id

    def get_name(self) -> str:
        return self.__name

    def set_name(self, new_name: str):
        self.__name = new_name

    def get_address(self) -> str:
        return self.__address

    def set_address(self, new_address: str):
        self.__address = new_address

    def get_cart(self) -> Cart:
        return self.__cart

    @property
    def name(self):
        return self.__name

    @property
    def address(self):
        return self.__address

    @property
    def cart(self):
        return self.__cart
