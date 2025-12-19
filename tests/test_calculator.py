import unittest

from src.calculator import Calculator


class CalculatorTests(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator(6, 4)

    def test_sum(self):
        assert self.calc.add() == 10

    def test_subtract(self):
        assert self.calc.sub() == 2

    def test_multiply(self):
        assert self.calc.mul() == 24

    def test_divide(self):
        assert self.calc.div() == 1.5
        # with self.assertRaises(ValueError):
        #    self.calc.div()

    # def test_divide_by_zero(self):
    #     with self.assertRaises(ValueError):
    #         self.calc.div()
