"""

Dynamic Polymorphism in real life says that 2 Objects coming from same
family will respond to same stimulus differently. Like in real world Manual
car and Electric car will respond to accelerate() differently.

To represent this in programming, we create a parent class that defines all
characters and behaviours that are generic to all child classes and are also same in
all child classes but make those methods abstract that are generic to all
child classes but all child class will behave differently. Then those child class
will provide implementation details of these abstract methods the way they want.
"""

from abc import ABC, abstractmethod

class Car(ABC):
    def __init__(self, brand: str, model: str, is_engine_on:bool = False, current_speed:int = 0):
        self._brand = brand
        self._model = model
        self._is_engine_on = is_engine_on
        self._current_speed = current_speed

    def start_engine(self) -> None:
        self._is_engine_on = True
        print(f"{self._brand} {self._model} - Engine started.")
    
    def stop_engine(self) -> None:
        self._is_engine_on = False
        self._current_speed = 0
        print(f"{self._brand} {self._model} - Engine stopped.")


    @abstractmethod
    def accelerate(self):
        pass

    @abstractmethod
    def apply_break(self):
        pass


class ManualCar(Car):
    def __init__(self, brand, model, is_engine_on = False, current_speed = 0, current_gear:int = 0):
        super().__init__(brand, model, is_engine_on, current_speed)
        self._current_gear = current_gear
    
    def shift_gear(self, gear:int):
        self._current_gear = gear
        print(f"{self._brand} {self._model} - Shifted to gear {self._current_gear}")

    def accelerate(self):
        if not self._is_engine_on:
            print(f"{self._brand} {self._model} - Cannot Accelerate, Engine is off!")
            return
        self._current_speed += 20
        print(f"{self._brand} {self._model} - Accelerating to {self._current_speed} km/hr")

    def apply_break(self):
        self._current_speed -= 20
        if self._current_speed < 0:
            self._current_speed = 0
        print(f"{self._brand} {self._model} - Breaking to {self._current_speed} km/hr")

class ElectricCar(Car):
    def __init__(self, brand, model, is_engine_on = False, current_speed = 0, battery_level:int = 100):
        super().__init__(brand, model, is_engine_on, current_speed)
        self._battery_level = battery_level
    
    def accelerate(self):
        if not self._is_engine_on:
            print(f"{self._brand} {self._model} - Cannot Accelerate, Engine is off!")
            return
        
        if self._battery_level <= 0:
            print(f"{self._brand} {self._model} - Cannot Accelerate, Battery is dead!")
            return
        self._battery_level -= 10
        self._current_speed += 15
        print(f"{self._brand} {self._model} - Accelerating to {self._current_speed} km/hr, Battery is at {self._battery_level}!")

    def charge_battery(self):
        self._batter_level = 100
        print(f"{self._brand} {self._model} - Battery fully charged")

    def apply_break(self):
        self._current_speed -= 15
        if self._current_speed < 0:
            self._current_speed = 0
        print(f"{self._brand} {self._model} - Regenerative braking! Speed is now {self._current_speed} km/hr.  Battery at {self._battery_level}%.")


if __name__ == "__main__":
    manual_car = ManualCar("Suzuki", "WagonR")
    manual_car.start_engine()
    manual_car.accelerate()
    manual_car.accelerate()
    manual_car.apply_break()
    manual_car.stop_engine()

    print("------------------------")


    electric_car = ElectricCar("Tesla", "Model S")
    electric_car.start_engine()
    electric_car.accelerate()
    electric_car.accelerate()
    electric_car.apply_break()
    electric_car.stop_engine()