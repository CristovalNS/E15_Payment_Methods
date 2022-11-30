class BankAccount:
    def __init__(self, name, balance, payment_method=None):
        self.__name = name
        self.__balance = balance
        self.__payment_method = payment_method

    def get_name(self):
        return self.__name

    def set_payment_method(self, payment_method):
        if payment_method == 10:
            self.__payment_method = 10
        elif payment_method == 5:
            self.__payment_method = 5
        return self.__payment_method

    def get_service_fee(self):
        if self.__payment_method == 10:
            return PaymentMethod(10).get_service_fee()
        elif self.__payment_method == 5:
            return PaymentMethod(5).get_service_fee()

    def get_balance(self):
        return self.__balance

    def pay(self, sum):
        if self.__balance > sum and PaymentMethod(CreditCard().CCservice_fee()):
            self.__balance = self.__balance - (sum + 10)
            return self.__balance
        elif self.__balance > sum and PaymentMethod(E_Wallet().EWservice_fee()):
            self.__balance = self.__balance - (sum + 5)
            return self.__balance

class PaymentMethod:
    def __init__(self, service_fee):
        self.__service_fee = service_fee

    def get_service_fee(self):
        return self.__service_fee

    def pay(self):
        pass


class CreditCard(PaymentMethod):
    def __init__(self, service_fee=10):
        PaymentMethod.__init__(self, service_fee)
        self.__CCservice_fee = service_fee

    def CCservice_fee(self):
        return self.__CCservice_fee


class E_Wallet(PaymentMethod):
    def __init__(self, service_fee=5):
        PaymentMethod.__init__(self, service_fee)
        self.__EWservice_fee = service_fee

    def EWservice_fee(self):
        return self.__EWservice_fee


# Testing
# x = CreditCard()
# print(x.CCservice_fee())
#
# x2 = PaymentMethod(CreditCard().CCservice_fee()).get_service_fee()
# print(x2)
#
# y = E_Wallet()
# print(y.EWservice_fee())
#
# y2 = PaymentMethod(E_Wallet().EWservice_fee()).get_service_fee()
# print(y2)
#
# print("*" * 40)
#
# John = BankAccount("John", 1000, "j")
# print(John.get_name())
# print(John.get_balance())
#
#
# mylist = ["User1", "User2", "User3"]
# user_input = input("Enter user: ")
