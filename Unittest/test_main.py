from main import add, subtract, multiply, divide
import unittest


class TestMain(unittest.TestCase):

    def test_add(self):
        self.assertTrue(add(5, 2))
        self.assertTrue(add("a", "b"))
        self.assertTrue(add(1.2, 3))
        self.assertEqual(add(5, 2), 7)

    def test_subtract(self):
        self.assertTrue(subtract(5, 2))
        self.assertEqual(subtract(12, 2), 10)

    def test_multiply(self):
        self.assertTrue(multiply(3, 2))
        self.assertEqual(multiply(3, 2), 6)

    def test_divide(self):
        self.assertTrue(divide(4, 2))
        self.assertFalse(divide(3, 0))
        self.assertEqual(divide(6, 2), 3)


if __name__ == '__main__':
    unittest.main()
