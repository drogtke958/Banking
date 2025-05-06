# Keily Drogt
# May 06, 2025
# Three Ways to Modify BankAccount Class Attributes

class BankAccount:
    """A simple class that models a bank account."""

    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f}. New balance is ${self.balance:.2f}.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f}. New balance is ${self.balance:.2f}.")
        else:
            print("Invalid withdrawal amount or insufficient funds!")

    def get_balance(self):
        return self.balance

    def display_account_info(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Account Balance: ${self.balance:.2f}")

my_account = BankAccount("Your Name", 1500)

my_account.display_account_info()
print()

my_account.balance = 2000
print("After direct assignment to balance:")
my_account.display_account_info()
print()

my_account.deposit(500)
my_account.display_account_info()
print()

my_account.withdraw(300)
my_account.display_account_info()
print()

my_account.withdraw(5000)
