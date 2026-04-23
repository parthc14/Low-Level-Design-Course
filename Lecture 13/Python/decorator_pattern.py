from abc import ABC, abstractmethod

class ICharacter(ABC):
    @abstractmethod
    def get_abilities(self) -> str:
        pass

class Mario(ICharacter):
    def get_abilities(self):
        return "Mario"


class IDecorator(ICharacter):
    def __init__(self, character: ICharacter):
        self.__character = character
    
    def get_character(self):
        return self.__character
    

class HeightUpDecorator(IDecorator):
    def __init__(self, character):
        super().__init__(character)
    
    def get_abilities(self):
        return self.get_character().get_abilities() + "with height up!"

class StarPowerDecorator(IDecorator):
    def __init__(self, character):
        super().__init__(character)
    
    def get_abilities(self):
        return self.get_character().get_abilities() + "with star power"
    

class GunPowerDecorator(IDecorator):
    def __init__(self, character):
        super().__init__(character)
    
    def get_abilities(self):
        return self.get_character().get_abilities() + "gun power!"


if __name__ == "__main__":
    mario = Mario()
    
    print(f"Basic character {mario.get_abilities()}")

    mario = HeightUpDecorator(mario)
    print(f"After Height up {mario.get_abilities()}")

    mario = GunPowerDecorator(mario)
    print(f"After Gunpower {mario.get_abilities()}")

    mario = StarPowerDecorator(mario)
    print(f"After StarPower {mario.get_abilities()}")
