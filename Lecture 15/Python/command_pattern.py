from abc import ABC, abstractmethod
from typing import List

class ICommand(ABC):
    
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass

class Light:
    def turn_on(self):
        print("Light is on")
    
    def turn_off(self):
        print("Light is now off")


class Fan:
    def turn_on(self):
        print("Fan is on")
    
    def turn_off(self):
        print("Fan is now off")


class LightCommand(ICommand):
    
    def __init__(self, light: Light):
        self.__light = light

    def get_light(self):
        return self.__light

    def execute(self):
        return self.get_light().turn_on()
    
    def undo(self):
        return self.get_light().turn_off()

class FanCommand(ICommand):
    
    def __init__(self, fan: Fan):
        self.__fan = fan

    def get_fan(self):
        return self.__fan

    def execute(self):
        return self.get_fan().turn_on()
    
    def undo(self):
        return self.get_fan().turn_off()

class RemoteController:
    num_buttons = 4

    def __init__(self):
        self.__buttons: List[ICommand] = [None] * RemoteController.num_buttons
        self.__button_pressed: List[bool] = [False] * RemoteController.num_buttons

    def get_buttons_list(self):
        return self.__buttons
    
    def get_current_button_state(self):
        return self.__button_pressed
    
    def set_command(self, idx: int, cmd: ICommand):
        if idx >= 0 and idx < RemoteController.num_buttons:
            self.get_buttons_list()[idx] = cmd
            self.get_current_button_state()[idx] = False

    def press_button(self, idx: int):
        if idx >= 0 and idx < RemoteController.num_buttons:
            if self.get_current_button_state()[idx] == False:
                self.get_buttons_list()[idx].execute()
                self.get_current_button_state()[idx] = True
            else:
                self.get_buttons_list()[idx].undo()
                self.get_current_button_state()[idx] = False
if __name__ == "__main__":
    living_room_light = Light()
    ceiling_fan = Fan()
    remote = RemoteController()
    

    remote.set_command(0, LightCommand(living_room_light))
    remote.set_command(1, FanCommand(ceiling_fan))

    print(f"----Toggling Light button 0-----")
    remote.press_button(0)
    remote.press_button(0)

    print(f"----Toggling Fan button 1-----")
    remote.press_button(1)
    remote.press_button(1)

    

