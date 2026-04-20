from strategies.PaymentStrategy import PaymentStrategy

class UPIStrategy(PaymentStrategy):
    def __init__(self, mobile_number: str):
        super().__init__()
        self.__mobile_number = mobile_number

    def pay(self, amount):
        print(f"Paid amount: {amount} using UPI")
