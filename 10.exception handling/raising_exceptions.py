print("\n--- Raising Exceptions ---")

class BankAccount:
    def __init__(self, balance):
        if not isinstance(balance, (int, float)) or balance < 0:
            raise ValueError("Balance must be number and not less than zero.")
        self.balance = balance
    
    def withdraw(self, amount):
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Amount must be number and greater than zero.")
        if amount > self.balance:
            raise ValueError("Balance is not enough.")
        self.balance -= amount
        print(f"Balance after withdraw: {self.balance}")

try:
    account1 = BankAccount(2000)
    print(f"Your balance: {account1.balance}")
    account1.withdraw(500)
    account1.withdraw(500)

    # Raise Exception
    print(f"Your withdraw amount is greater than balance {account1.balance}")
    account1.withdraw(1500)
    

except ValueError as e:
    print(f"Back Account Error: {e}")
except Exception as e:
    print(f"Unexcepted Error: {e}")

