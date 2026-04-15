"""
/*
Car Interface --> Act as an interface for Outsiude world to operate the car. 
This interface tells 'WHAT' all it can do rather then 'HOW' it does that.
Since this is an interface we cannot directly create Objects of this. We
need to implement it first and then that child class will have the responsibility to 
provide implementation details of all the methods in the interface.

In our real world example of Car, imagine you sitting in the car and able to operate
the car (startEngine, accelerate, brake, turn) just by pressing or moving some
pedals/buttons/stearing wheel etc. You dont need to know how these things work, and
also they are hidden under thre hood.
This Interface 'Car' denotes that (pedals/buttons/stearing wheel etc). 
*/

"""

from abc import ABC, abstractmethod

class Car(ABC):
    @abstractmethod
    def start_engine(self) -> None:
        pass
    
    @abstractmethod
    def shift_gear(self, gear: int) -> None:
        pass

    @abstractmethod
    def accelerate(self) -> None:
        pass

    @abstractmethod
    def apply_break(self)-> None:
        pass

    @abstractmethod
    def stop_engine(self) -> None:
        pass

"""
This is a Concrete class (A class that provide implementation details of an interface/abstract class).
Now anyone can make an Object of 'SportsCar' and can assign it to 'Car' reference. 
(See main method for this)

In our real world example of Car, as you cannot have a real car by just having its body only
(all these buttons or pedals). You need to have the actual implementation of 'What' happens
when we press these buttons. 'SportsCar' class denotes that actual implementation. 

Hence we can concude, to denote a real world car in programming we created 2 classes.
One to deonte all the user-interface like pedals, buttons, stearing wheels etc ('Car' interface).
And another one to denote the actual car with all the implementations of these buttons (SportsCar' class).
"""

class SportsCar(Car):
    def __init__(self, brand: str, model: str, is_engine_on: bool = False, current_speed: int = 0, current_gear: int = 0):
        super().__init__()
        self.brand = brand
        self.model = model
        self.current_speed = current_speed
        self.is_engine_on = is_engine_on
        self.current_gear = current_gear

    def start_engine(self):
        self.is_engine_on = True
        print(f"{self.brand} {self.model} : Engine starts with a roar")

    def shift_gear(self, gear):
        if not self.is_engine_on:
            print(f"{self.brand} {self.model} : Engine is off, cannot start engine")
            return
        self.current_gear = gear
        print(f"${self.brand} {self.model} : Shifted to gear {self.current_gear}")

    def accelerate(self):
        if not self.is_engine_on:
            print(f"{self.brand} {self.model} : Engine is off, cannot accelerate")
            return
        self.current_speed += 20
        print(f"{self.brand} {self.model} : Accelerating to {self.current_speed} km/hr")
            
    
    def apply_break(self):
        self.current_speed -= 20
        if self.current_speed < 0:
            self.current_speed = 0
        print(f"{self.brand} {self.model} : Breaking! Speed is now {self.current_speed} km/hr") 

    
    def stop_engine(self):
        self.current_gear = 0
        self.is_engine_off = False
        self.current_speed = 0
        print(f"{self.brand} {self.model} : Engine turned off")


if __name__ == "__main__":
    c = SportsCar("Fort", "Mustang")
    c.start_engine()
    c.shift_gear(1)
    c.accelerate()
    c.shift_gear(2)
    c.accelerate()
    c.apply_break()
    c.stop_engine()



