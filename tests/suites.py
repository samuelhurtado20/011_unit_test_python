import unittest

from tests.test_bank import BankAccountTests


def bank_account_test_suite():
    suite = unittest.TestSuite()
    suite.addTest(BankAccountTests("test_deposit"))
    suite.addTest(BankAccountTests("test_withdraw"))
    return suite


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(bank_account_test_suite())
