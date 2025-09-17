class BankAccount:
    # Constructor
    def __init__(self, account_number, holder_name, balance=0):
        self.__account_number = account_number   # private attribute
        self.holder_name = holder_name
        self.__balance = balance                 # private attribute

    # Deposit money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}, New Balance: {self.__balance}")
        else:
            print("Deposit amount must be positive!")

    # Withdraw money
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn: {amount}, Remaining Balance: {self.__balance}")
        else:
            print("Insufficient balance or invalid amount!")

    # Getter for balance (encapsulation)
    def get_balance(self):
        return self.__balance


# Inheritance Example
class SavingsAccount(BankAccount):
    def __init__(self, account_number, holder_name, balance=0, interest_rate=5):
        super().__init__(account_number, holder_name, balance)
        self.interest_rate = interest_rate

    # Add interest (method overriding = polymorphism)
    def add_interest(self):
        interest = self.get_balance() * (self.interest_rate / 100)
        self.deposit(interest)
        print(f"Interest of {interest} added!")


# ---- Usage ----
acc1 = BankAccount("12345", "Rohit", 1000)
acc1.deposit(500)
acc1.withdraw(200)
print("Balance:", acc1.get_balance())

print("-----")

acc2 = SavingsAccount("67890", "Anita", 2000, 10)
acc2.deposit(1000)
acc2.add_interest()
print("Balance after interest:", acc2.get_balance())
