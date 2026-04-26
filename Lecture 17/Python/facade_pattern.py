class PowerSupply:
    def provide_power(self):
        print(f"Power supply: Providing power")

class CoolingSystem:
    def start_fans(self):
        print(f"Cooling system: Fans started")
    
class CPU:
    def initialize(self):
        print(f"CPU: Initialize Started")

class Memory:
    def self_test(self):
        print(f"Memory: Self-Test passed")

class HardDrive:
    def spin_up(self):
        print(f"HardDrive: Spinning up..")

class BIOS:
    def boot(self, cpu: CPU, memory: Memory):
        print("BIOS: Booting CPU and memory checks...")
        cpu.initialize()
        memory.self_test()

class OS:
    def load(self):
        print("OS: Loading into memory")

class ComputerFacade:
    __power_supply = PowerSupply()
    __cooling_system = CoolingSystem()
    __cpu = CPU()
    __memory = Memory()
    __hard_drive = HardDrive()
    __bios = BIOS()
    __os = OS()


    def start_computer(self):
        print("---- Starting Computer -------")
        self.__power_supply.provide_power()
        self.__cooling_system.start_fans()
        self.__bios.boot(self.__cpu, self.__memory)
        self.__hard_drive.spin_up()
        self.__os.load()
        print("---- Computer Started Successfully")


if __name__ == "__main__":
    computer_facade = ComputerFacade()
    computer_facade.start_computer()