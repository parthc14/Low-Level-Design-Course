from strategies.PaymentStrategy import PaymentStrategy

class CreditCardStrategy(PaymentStrategy):
    def __init__(self, credit_card_number: int):
        super().__init__()
        self.__credit_card_number = credit_card_number

    def pay(self, amount):
        return print(f"Amount {amount} paid using credit card..")