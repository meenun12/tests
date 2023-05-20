import unittest
from calculator import Calculator

class TestsCalculator(unittest.TestCase):
    def test_add_functionality(self):
        calc = Calculator(10, 20)
        result = calc.calc_add()
        self.assertEqual(result, 30)

    def test_add_functionality_two_negative_numbers(self):
        calc = Calculator(-10, -20)
        result = calc.calc_add()
        self.assertEqual(result, -20)









