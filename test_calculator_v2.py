import unittest
import calculator

class TestsCalculator2(unittest.TestCase):

    def test_add_functionality(self):
        calc1 = Calculator(10, 30)
        result = calc1.calc_add()
        self.assertEqual(result, 40)

    def test_add_functionality_two_negative_numbers(self):
        result = calculator.calc_add(10, -30)
        result = calc1.calc_add()
        self.assertEqual(result, -20)




