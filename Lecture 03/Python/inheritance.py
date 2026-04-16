"""
We know that real world Objects show inheritance relationship where we
have parent object and child object. child object have all the characters
or behaviours that parent have plus some additional characters/behaviours.
Like all cars in real world have a brand, model etc and can start, stop, 
accelerate etc. But some specific cars like manual car have gear System
while other specific cars like Electric cars have battery system.

We represent this scenario of real world in programming by creating a parent class and
defining all the characters(variables) or behaviours(methods) that all cars 
have in parent class. Then we create different child classes that inherits 
from this parent class and define only those characters and behaviours
that are specific to them. Although objects of these child classes can 
access or call parent class characters(variables) and behaviours(methods).
Hence providing code reusability.
"""
class Car:
    def __init__(self, brand: str, model:str, is_engine_on:bool = False, current_speed: int = 0):
        self._brand = brand
        self._model = model
        self._is_engine_on = is_engine_on
        self._current_speed = current_speed

    def start_engine(self):
        self._is_engine_on = True
        print(f"Starting the engine for {self._brand} and {self._model}")

    def stop_engine(self):
        if not self._is_engine_on:
            print(f"Cannot stop an already stopped engine")
        self._is_engine_on = False
        print(f"Engine turned off for the {self._brand} {self._model}")
    
    def accelerate(self):
        if not self._is_engine_on:
            print("Cannot accelerate as engine is off!")
        self._current_speed += 20
        print(f"Accelerating to speed of {self._current_speed} km/hr")
    
    def apply_breake(self):
        if not self._is_engine_on:
            print("Cannot decelerate as engine is off")
        
        if(self._current_speed < 0):
            self._current_speed -= 20
        self._current_speed -= 20
        print(f"Deccelerating to speed of {self._current_speed} km/hr")

class ManualCar(Car):
    def __init__(self, brand, model, is_engine_on = False, current_speed = 0, current_gear:int = 0):
        super().__init__(brand, model, is_engine_on, current_speed)
        self._current_gear = current_gear

    def shift_gear(self, gear: int):
        self._current_gear = gear
        print(f"Shifted to gear: {self._current_gear} for {self._brand} {self._model}")
    
class BatteryCar(Car):
    def __init__(self, brand, model, is_engine_on = False, current_speed = 0, battery_level = 100):
        super().__init__(brand, model, is_engine_on, current_speed)
        self._battery_level = battery_level
    
    def charge_battery(self):
        self._battery_level = 100
        print(f"Battery fully charged for {self._brand} {self._model}")


if __name__ == "__main__":
    mc = ManualCar("Suzuki", "WagonR")

    mc.start_engine()
    mc.accelerate()
    mc.shift_gear(1)
    mc.accelerate()
    mc.accelerate()
    mc.shift_gear(2)
    mc.apply_breake()
    mc.stop_engine()


    print("------------")

    ec = BatteryCar("Tesla", "Y")
    ec.start_engine()
    ec.accelerate()
    ec.accelerate()
    ec.charge_battery()
    ec.apply_breake()
    ec.stop_engine()

    

    
