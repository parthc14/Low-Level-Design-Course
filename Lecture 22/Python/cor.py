from abc import ABC, abstractmethod
from typing import Optional

class MoneyHandler(ABC):
    def __init__(self):
        self.next_handler: Optional[MoneyHandler] = None

    def set_next_handler(self, next_handler: MoneyHandler):
        self.next_handler = next_handler

    @abstractmethod
    def dispense(self, amnt: int):
        pass


class ThousandHandler(MoneyHandler):
    def __init__(self, num_notes: int):
        super().__init__()
        self.num_notes = num_notes

    def dispense(self, amnt):
        notes_needed = amnt // 1000

        if notes_needed > self.num_notes:
            notes_needed = self.num_notes
            self.num_notes = 0
        else:
            self.num_notes -= notes_needed
    
        if notes_needed > 0:
            print(f"Dispensing {notes_needed} x 1000 notes")

        remaining = amnt - (notes_needed * 1000)
        if remaining > 0:
            if self.next_handler is not None:
                self.next_handler.dispense(remaining)
            else:
                print(f"Remaining amnt of {remaining} cannot be dispensed")


class TwoHunderHandler(MoneyHandler):
    def __init__(self, num_notes: int):
        super().__init__()
        self.num_notes = num_notes

    def dispense(self, amnt):
        notes_needed = amnt // 200

        if notes_needed > self.num_notes:
            notes_needed = self.num_notes
            self.num_notes = 0
        else:
            self.num_notes -= notes_needed
    
        if notes_needed > 0:
            print(f"Dispensing {notes_needed} x 200 notes")

        remaining = amnt - (notes_needed * 200)
        if remaining > 0:
            if self.next_handler is not None:
                self.next_handler.dispense(remaining)
            else:
                print(f"Remaining amnt of {remaining} cannot be dispensed")

class FiveHundredHandler(MoneyHandler):
    def __init__(self, num_notes: int):
        super().__init__()
        self.num_notes = num_notes

    def dispense(self, amnt):
        notes_needed = amnt // 500

        if notes_needed > self.num_notes:
            notes_needed = self.num_notes
            self.num_notes = 0
        else:
            self.num_notes -= notes_needed
    
        if notes_needed > 0:
            print(f"Dispensing {notes_needed} x 500 notes")

        remaining = amnt - (notes_needed * 500)
        if remaining > 0:
            if self.next_handler is not None:
                self.next_handler.dispense(remaining)
            else:
                print(f"Remaining amnt of {remaining} cannot be dispensed")

class HundredHandler(MoneyHandler):
    def __init__(self, num_notes: int):
        super().__init__()
        self.num_notes = num_notes

    def dispense(self, amnt):
        notes_needed = amnt // 100

        if notes_needed > self.num_notes:
            notes_needed = self.num_notes
            self.num_notes = 0
        else:
            self.num_notes -= notes_needed
    
        if notes_needed > 0:
            print(f"Dispensing {notes_needed} x 100 notes")

        remaining = amnt - (notes_needed * 100)
        if remaining > 0:
            if self.next_handler is not None:
                self.next_handler.dispense(remaining)
            else:
                print(f"Remaining amnt of {remaining} cannot be dispensed")


if __name__ == "__main__":
    thousand_handler = ThousandHandler(3)
    five_hundred_handler = FiveHundredHandler(5)
    two_hundred_handler = TwoHunderHandler(10)
    one_hundred_handler = HundredHandler(20)

    # Set chain of responsibility.
    thousand_handler.set_next_handler(five_hundred_handler)
    five_hundred_handler.set_next_handler(two_hundred_handler)
    two_hundred_handler.set_next_handler(one_hundred_handler)

    amnt_to_with_draw = 10000

    print(f"Dispensing amount: ${amnt_to_with_draw}")
    thousand_handler.dispense(amnt_to_with_draw)