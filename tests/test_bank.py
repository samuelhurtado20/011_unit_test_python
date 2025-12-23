import datetime
import os
import unittest

from unittest.mock import patch

from src.bank import BankAccount, InsufficientFundsError, WithdrawalTimeRestrictionError

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

    @patch("src.bank.datetime")
    def test_withdraw(self, mock_datetime):
        mock_datetime.now.return_value = datetime.datetime(2025, 12, 19, 10, 0)
        new_balance = self.account.withdraw(200)
        assert new_balance == 800

    @patch("src.bank.datetime")
    def test_withdraw_with_deposit(self, mock_datetime):
        mock_datetime.now.return_value = datetime.datetime(2025, 12, 19, 10, 0)
        # mock_datetime.now.return_value.hour.return_value = 10
        self.account.deposit(200)
        self.account.withdraw(50)
        self.assertEqual(self.account.balance, 1150)

    def test_get_balance(self):
        assert self.account.get_balance() == 1000

    @patch("src.bank.datetime")
    def test_withdraw_insufficient_funds(self, mock_datetime):
        mock_datetime.now.return_value = datetime.datetime(2025, 12, 19, 10, 0)
        self.account.deposit(500)
        with self.assertRaises(InsufficientFundsError):
            self.account.withdraw(2000)

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

    @patch("src.bank.datetime")
    def test_withdraw_on_weekday(self, mock_datetime):
        mock_datetime.now.return_value = datetime.datetime(2025, 12, 19, 10, 0)
        balance = self.account.get_balance()
        new_balnace = self.account.withdraw(50)
        self.assertEqual(new_balnace, balance - 50)

    @patch("src.bank.datetime")
    def test_withdraw_on_weekend(self, mock_datetime):
        mock_datetime.now.return_value.weekday.return_value = 6
        with self.assertRaises(WithdrawalTimeRestrictionError):
            self.account.withdraw(50)

    @patch("src.bank.datetime")
    def test_withdraw_after_10pm(self, mock_datetime):
        mock_datetime.now.return_value = datetime.datetime(2025, 12, 19, 22, 0)
        with self.assertRaises(WithdrawalTimeRestrictionError):
            self.account.withdraw(50)

    @patch("src.bank.datetime")
    def test_withdraw_before_8am(self, mock_datetime):
        mock_datetime.now.return_value = datetime.datetime(2025, 12, 19, 7, 0)
        with self.assertRaises(WithdrawalTimeRestrictionError):
            self.account.withdraw(50)

    def test_several_deposits(self):
        test_cases = [
            {"amount": 100, "expected_balance": 1100},
            {"amount": 200, "expected_balance": 1200},
            {"amount": 300, "expected_balance": 1300},
        ]
        for case in test_cases:
            with self.subTest(case=case):
                self.account = BankAccount(initial_balance=1000)
                new_balance = self.account.deposit(case["amount"])
                self.assertEqual(new_balance, case["expected_balance"])
