"""
Static Polymorphism (Compile-time polymorphism) in real life says that
the same action can behave differently depending on the input parameters.
For example, a Manual car can accelerate by a fixed amount or by a
specific amount you request. In programming, we achieve this via method
overloading: multiple methods with the same name but different signatures.
"""

from typing import overload, Optional
class ManualCar:
    def __init__(self, brand:str, model:str, is_engine_on: bool = False, current_speed:int = 0, current_gear:int = 0):
        self._brand = brand
        self._model = model
        self._is_engine_on = is_engine_on
        self._current_speed = current_speed
        self._current_gear = current_gear
    
    def start_engine(self) -> None:
        self._is_engine_on = True
        print(f"{self._model} {self._brand}: Engine started")

    def stop_engine(self) -> None:
        self._is_engine_on = False
        self._current_speed = 0
        print(f"{self._model} {self._brand}: Engine turned off")

    """
    This is one of the approach to do operator overloading in python, by defining default
    options. This is pythonic.
    """
    # def accelerate(self, speed: int = 20) -> None:
    #     if not self._is_engine_on:
    #         print(f"{self._brand} {self._model} cannot accelerate! Engine is off")
    #         return
    #     self._current_speed += speed
    #     print(f"{self._brand} {self._model} accelerating to {self._current_speed} km/hr")

    """
    This is a way of skipping overloading. Not pythonic. You have to define three functions
    """
    @overload
    def accelerate(self, speed:int) -> None:
        """Signature for custom acceleration."""

    @overload
    def accelerate(self) -> None:
        """Signature for custom acceleration."""
    
    def accelerate(self, speed: Optional[int] = None) -> None:
        if not self._is_engine_on:
            print(f"{self._brand} {self._model} cannot accelerate! Engine is off")
            return
        increment = speed if speed is not None else 20
        self._current_speed += increment
        print(f"{self._brand} {self._model} accelerating to {self._current_speed} km/hr")

    def apply_break(self) -> None:
        self._current_speed -= 20
        if self._current_speed < 0:
            self._current_speed = 0
        print(f"{self._brand} {self._model} breaking! Speed is not {self._current_speed} km/hr")

    def shift_gear(self, gear: int) -> None:
        self._current_gear = gear
        print(f"{self._brand} {self._model} shifted to gear {self._current_gear}")


if __name__ == "__main__":
    manualCar = ManualCar("Suzuki", "WagonR")
    manualCar.start_engine()
    manualCar.accelerate()
    manualCar.accelerate(40)
    manualCar.apply_break()
    manualCar.stop_engine()
