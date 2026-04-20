class MenuItem:
    def __init__(self, code: int, name: str, price: float):
        self.__code = code
        self.__name = name
        self.__price = price

    def get_code(self) -> int:
        return self.__code

    def set_code(self, new_code: int) -> None:
        self.__code = new_code

    def get_name(self) -> str:
        return self.__name

    def set_name(self, new_name: str) -> None:
        self.__name = new_name

    def get_price(self) -> float:
        return self.__price

    def set_price(self, new_price: float) -> None:
        self.__price = new_price

    @property
    def price(self) -> float:
        return self.__price

    @property
    def name(self) -> str:
        return self.__name
