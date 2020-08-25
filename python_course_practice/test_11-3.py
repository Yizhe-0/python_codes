import unittest
from employee11_3 import Employee


class TestEmployee(unittest.TestCase):
    """Tests for the class Employee."""

    def setUp(self):
        """Make an employee to use."""
        self.me = Employee('yizhe', 'niu', 10000)

    def test_give_default_raise(self):
        """Test if get_default_raise working."""
        self.me.give_raise()
        self.assertEqual(self.me.salary, 15000)

    def test_give_custom_raise(self):
        self.me.give_raise(20000)
        self.assertEqual(self.me.salary, 30000)


unittest.main()
