import unittest
import calculator

class TestsCalculatorAddFunctionality(unittest.TestCase):

    def add_two_positive_numbers(self):
        calc = Calculator(10, 30)
        result = calc.calc_add()
        self.assertEqual(result, 30)

    def add_one_positive_number_and_one_negative(self):
        calc = Calculator(50, -90)
        result = calc.calc_add()
        self.assertEqual(result, -40)

    def test_add_two_negative_numbers(self):
        calc = Calculator(-10, -20)
        result = calc.calc_add()
        self.assertEqual(result, -30)







