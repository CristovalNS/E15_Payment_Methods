from payment_method import PaymentMethod

class BankAccount:
    def __init__(self, name, balance, payment_method):
        self.__name = name
        self.__balance = balance
        self.__payment_method = payment_method

    def get_name(self):
        pass

    def set_payment_method(self):
        pass

    def get_service_fee(self):
        # Should be from payment class
        return PaymentMethod().get_service_fee()

    def get_balance(self):
        return self.__balance

    def pay(self):
        pass