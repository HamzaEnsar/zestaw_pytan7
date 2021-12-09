from main2 import Employee
import unittest


class TestMain2(unittest.TestCase):
    def setUp(self):
        self.emp1 = Employee("Hamza", "Ensar", 23, 1000)
        self.emp2 = Employee("Hamza", "Ensar", 23, 100)
        self.emp3 = Employee("Tyson", "Shan", 13, 25)

    def test_introduce_self(self):
        self.assertTrue(Employee.introduce_self(self.emp1))
        self.assertEqual(Employee.introduce_self(self.emp1), Employee.introduce_self(self.emp2))

    def test_raise_salary(self):
        self.assertIsNone(Employee.raise_salary(self.emp1, 1.2))
        self.assertEqual(Employee.raise_salary(self.emp1, 1), Employee.raise_salary(self.emp2, 10))

    def test_check_age(self):
        self.assertTrue(Employee.check_age(self.emp1))
        self.assertFalse(Employee.check_age(self.emp3))
        self.assertEqual(Employee.check_age(self.emp1), Employee.check_age(self.emp2))

    def test_get_email(self):
        self.assertTrue(Employee.get_email(self.emp1))
        self.assertEqual(Employee.get_email(self.emp1), Employee.get_email(self.emp2))


if __name__ == '__main__':
    unittest.main()
