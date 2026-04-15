"""
Encapsulation says 2 things:
1. An Object's Characteristics and its behaviour are encapsulated together
within that Object.
2. All the characteristics or behaviours are not for everyone to access.
Object should provide data security.

We follow above 2 pointers about Object of real world in programming by:
1. Creating a class that act as a blueprint for Object creation. Class contain
all the characteristics (class variable) and behaviour (class methods) in one block,
encapsulating it together.
2. We introduce access modifiers (public, private, protected, default) etc to provide data
security to the class members.
"""

class SportsCar():
    def __init__(self, brand: str, model: str, is_engine_on: bool = False, current_speed: int = 0, current_gear: int = 0):
        self.__brand = brand
        self.__model = model
        self.__current_speed = current_speed
        self.__is_engine_on = is_engine_on
        self.__current_gear = current_gear

    def start_engine(self):
        self.__is_engine_on = True
        print(f"{self.__brand} {self.__model} : Engine starts with a roar")

    def shift_gear(self, gear):
        if not self.__is_engine_on:
            print(f"{self.__brand} {self.__model} : Engine is off, cannot start engine")
            return
        self.__current_gear = gear
        print(f"${self.__brand} {self.__model} : Shifted to gear {self.__current_gear}")

    def accelerate(self):
        if not self.__is_engine_on:
            print(f"{self.__brand} {self.__model} : Engine is off, cannot accelerate")
            return
        self.__current_speed += 20
        print(f"{self.__brand} {self.__model} : Accelerating to {self.__current_speed} km/hr")
            
    
    def apply_break(self):
        self.__current_speed -= 20
        if self.__current_speed < 0:
            self.__current_speed = 0
        print(f"{self.__brand} {self.__model} : Breaking! Speed is now {self.__current_speed} km/hr") 

    
    def stop_engine(self):
        self.__current_gear = 0
        self.__is_engine_on = False
        self.__current_speed = 0
        print(f"{self.__brand} {self.__model} : Engine turned off")


if __name__ == "__main__":
    c = SportsCar("Fort", "Mustang")
    c.start_engine()
    c.shift_gear(1)
    c.accelerate()
    c.shift_gear(2)
    c.accelerate()
    c.apply_break()
    c.stop_engine()



