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

class GarlicBread(ABC):
    @abstractmethod
    def prepare(self):
        pass

class BasicGarlicBread(GarlicBread):
    def prepare(self):
        print("Just a basic garlic bread")

class CheeseGarlicBread(GarlicBread):
    def prepare(self):
        print("Just a basic garlic bread with cheese")

class WheatGarlicBread(GarlicBread):
    def prepare(self):
        print("Just a wheat garlic bread with cheese")



class SinghBurger():
    def create_burger(self, type):
        if type == "basic":
            return BasicBurger()
        elif type == "standard":
            return StandardBurger()
        elif type == "premium":
            return PremiumBurger()
    
    def create_garlic_bread(self, type):
        if type == "basic":
            return BasicGarlicBread()
        elif type == "standard":
            return CheeseGarlicBread()
        elif type == "premium":
            return WheatGarlicBread()

if __name__ == "__main__":
    burgerType = "basic"
    garlic_bread = "standard"

    singh_burger = SinghBurger()
    burger = singh_burger.create_burger(burgerType)
    garlic_bread = singh_burger.create_garlic_bread(garlic_bread)
    
    burger.prepare()
    garlic_bread.prepare()





