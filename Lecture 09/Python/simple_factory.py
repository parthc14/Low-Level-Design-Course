from abc import ABC, abstractmethod

class Burger(ABC):
    @abstractmethod
    def prepare(self):
        pass

class BasicBurger(Burger):
    def prepare(self):
        print("Just a basic burger with patty")
    
class StandardBurger(Burger):
    def prepare(self):
        print("Burger with patty and veggies!")
    
class PremiumBurger(Burger):
    def prepare(self):
        print("Burger with patty, veggies and extra cheese")


class FactoryBurger():
    def __init__(self, type_of_burger: Burger):
        self._burger_type = type_of_burger

    def create_burger(self) -> Burger:
        if self._burger_type == "basic":
            return BasicBurger()
        elif self._burger_type == "standard":
            return StandardBurger()
        elif self._burger_type == "premium":
            return PremiumBurger()

if __name__ == "__main__":
    factory = FactoryBurger("basic")
    burger_type = factory.create_burger()
    burger_type.prepare()

    print("-------------")

    factory1 = FactoryBurger("standard")
    burger_type1 = factory1.create_burger()
    burger_type1.prepare()

    print("-------------")

    factory2 = FactoryBurger("premium")
    burger_type2 = factory2.create_burger()
    burger_type2.prepare()




