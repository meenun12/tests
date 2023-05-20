import unittest
from unit_testing_02.calculator_v3 import Calculator

class TestsCalculatorAddFunctionality(unittest.TestCase):

    def setUp(self) -> None:
        print("setup invoked!")

    def tearDown(self) -> None:
        print("tearDown invoked!")

    def test_add_two_positive_numbers(self):
        print(">>> test_add_two_positive_numbers")
        calc = Calculator(10, 30)
        result = calc.calc_add()
        self.assertEqual(result, 40)

    def test_add_one_positive_number_and_one_negative(self):
        print(">>> test_add_one_positive_number_and_one_negative")
        calc = Calculator(50, -90)
        result = calc.calc_add()
        self.assertEqual(result, -40)

    def test_add_two_negative_numbers(self):
        calc = Calculator(-10, -20)
        result = calc.calc_add()
        self.assertEqual(result, -30)







