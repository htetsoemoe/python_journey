class BankAccount:
    def __init__(self, account_number, initial_balance):
        self.account_number = account_number # Public
        self._balance = initial_balance # Protected (Conventional not to be change from outside)
        self.__pin = "1234" # Private (different to access directly)

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"After deposit, balance: {self._balance}")
        else:
            print("Please enter a valid amount.")

    def withdraw(self, amount, pin):
        if pin == self.__pin: # Can only withdraw if the PIN is correct
            if self._balance >= amount > 0:
                self._balance -= amount
                print(f"After withdrawal, balance: {self._balance}")
            else:
                print("Insufficient balance or incorrect amount.")
        else:
            print("Incorrect PIN number.")

    def get_balance(self): # Public method to get the balance
        return self._balance
    
# Creating an object and testing
my_account = BankAccount("123-456-789", 1000)

print(f"Account number: {my_account.account_number}")
# print(my_account._balance) # This works but should not be done (by convention)
# print(my_account.__pin) # Will raise an AttributeError (cannot be accessed directly)

my_account.deposit(500)
my_account.withdraw(200, "1234")
my_account.withdraw(1000, "0000") # Will not withdraw due to incorrect PIN

print(f"Current balance: {my_account.get_balance()}")