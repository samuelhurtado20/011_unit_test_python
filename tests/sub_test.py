import unittest


def is_even(n):
    return n % 2 == 0


class TestMathUtils(unittest.TestCase):
    def test_is_even(self):
        test_cases = [(2, True), (3, False), (0, True), (-4, True), (-1, False)]
        for value, expected in test_cases:
            with self.subTest(value=value):
                self.assertEqual(is_even(value), expected)
