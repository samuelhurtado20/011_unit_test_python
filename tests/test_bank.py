import os
import unittest

from src.bank import BankAccount

# $env:PYTHONPATH = "."; python .\testS\test_suites.py
# python -m unittest tests.test_calculator.CalculatorTests.test_sum
# python -m unittest discover tests


class BankAccountTests(unittest.TestCase):

    def setUp(self) -> None:
        self.account = BankAccount(initial_balance=1000)

    def tearDown(self) -> None:
        if os.path.exists(self.account.log_file):
            os.remove(self.account.log_file)

    def _count_lines(self, file_path):
        with open(file_path, "r") as file:
            return sum(1 for line in file)

    def test_initial_balance(self):
        assert self.account.balance == 1000

    def test_deposit(self):
        new_balance = self.account.deposit(500)
        assert new_balance == 1500

    def test_withdraw(self):
        new_balance = self.account.withdraw(200)
        assert new_balance == 800

    def test_withdraw_with_deposit(self):
        account = BankAccount()
        account.deposit(200)
        account.withdraw(50)
        assert account.balance == 150

    def test_get_balance(self):
        assert self.account.get_balance() == 1000

    def test_withdraw_insufficient_funds(self):
        account = BankAccount()
        account.deposit(50)
        with self.assertRaises(ValueError):
            account.withdraw(100)

    # ✅ Transferencia exitosa
    def test_transfer_successful(self):
        target = BankAccount(initial_balance=200)
        self.account.transfer(300, target)
        assert self.account.get_balance() == 700
        assert target.get_balance() == 500

    # ❌ Transferencia fallida por fondos insuficientes
    def test_transfer_insufficient_funds(self):
        target = BankAccount(initial_balance=100)
        with self.assertRaises(ValueError):
            self.account.transfer(2000, target)

    # ✅ Transferencia fallida por monto negativo
    def test_transfer_negative_amount(self):
        target = BankAccount(initial_balance=100)
        with self.assertRaises(ValueError):
            self.account.transfer(-100, target)

    def test_transaction_log_exists(self):
        self.account.deposit(100)
        assert os.path.exists(self.account.log_file)
