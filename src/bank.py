class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance
        self.log_file = "transactions.log"
        self._log_transaction("Account created")

    def _log_transaction(self, message):
        if self.log_file:
            with open(self.log_file, "a") as f:
                f.write(f"{message} \n")

    def deposit(self, amount):
        if amount > 0:
            self._log_transaction(f"Deposited {amount}")
            self.balance += amount
        else:
            self._log_transaction(f"Failed to deposit {amount}")
            raise ValueError("Deposit amount must be positive")
        self._log_transaction(f"Deposited {amount}")
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            self._log_transaction(f"Failed to withdraw {amount}")
            raise ValueError("Insufficient funds")
        elif amount <= 0:
            self._log_transaction(f"Failed to withdraw {amount}")
            raise ValueError("Withdrawal amount must be positive")
        else:
            self.balance -= amount
        self._log_transaction(f"Withdrew {amount}")
        return self.balance

    def get_balance(self):
        self._log_transaction(f"Balance checked amount: {self.balance}")
        return self.balance

    def transfer(self, amount, target_account):
        if amount <= 0:
            self._log_transaction(f"Failed to transfer {amount} to {target_account}")
            raise ValueError("Transfer amount must be positive")
        if amount > self.balance:
            self._log_transaction(f"Failed to transfer {amount} to {target_account}")
            raise ValueError("Insufficient funds for transfer")
        self.balance -= amount
        target_account.deposit(amount)
        self._log_transaction(f"Transferred {amount} to {target_account}")
        return self.balance
