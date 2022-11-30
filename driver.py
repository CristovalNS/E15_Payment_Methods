from payment_method import BankAccount, PaymentMethod, CreditCard, E_Wallet

restaurant = {
    "burger": 10,
    "softdrink": 5,
    "pizza": 15 }
transaction_id = 0


def transaction(customer, items):
    global transaction_id
    transaction_id += 1
    print("*" * 30)
    print(f"Transaction ID: #{transaction_id:02d}")
    print(f"Customer: {customer.get_name()}")
    print(f"Starting Balance: ${customer.get_balance():.2f}")
    print("*" * 30)
    sum = 0
    for item in items:
        print(f"{item}: ${restaurant[item]:.2f}")
        sum += restaurant[item]
    print("*" * 30)
    print(f"Sub Total: ${sum:.2f}")
    print(f"Service fee: ${(customer.get_service_fee()):.2f}")
    print(f"Total: ${(sum + customer.get_service_fee()):.2f}")
    print("*" * 30)
    customer.pay(sum)
    print(f"Ending Balance: ${(customer.get_balance()):.2f}")
    print("*" * 30)
    print()


john = BankAccount("John", 100)
john.set_payment_method(CreditCard().CCservice_fee())
transaction(john, ["burger", "pizza", "softdrink"])

jane = BankAccount("Jane", 100)
jane.set_payment_method(E_Wallet().EWservice_fee())
transaction(jane, ["pizza", "softdrink"])
