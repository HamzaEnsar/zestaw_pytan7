from main3 import is_numeric, is_negative, calculate_savings
import unittest


class TestMain3(unittest.TestCase):

    def test_is_numeric(self):
        self.assertTrue(is_numeric(3))
        self.assertFalse(is_numeric("a"))

    def test_is_negative(self):
        self.assertTrue(is_negative(-3))
        self.assertFalse(is_negative(6))

    def test_calculate_savings(self):
        self.assertTrue(calculate_savings(100, 200, 50))
        self.assertFalse(calculate_savings(-100, 200, 100))
        self.assertFalse(calculate_savings(100, "a", 50))


if __name__ == '__main__':
    unittest.main()
