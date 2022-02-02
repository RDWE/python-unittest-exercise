from exampleCode.calculator import Calculator
import unittest 

class CalculatorulatorMethods(unittest.TestCase): 

    def test_addition(self): 
        result = Calculator.add(1,2)
        self.assertEqual(result, 3)

    def test_subtraction(self):
        result = Calculator.subtract(2, 1)
        self.assertEqual(result, 1)

    def test_multiply(self): 
        result = Calculator.multiply(456, 987)
        self.assertEqual(result, 450072)

    def test_division(self): 
        result = Calculator.divide(99,3)
        self.assertEqual(result, 33)

    def test_divide_by_zero(self):
        """You add arguments to the assertRaises call"""
        self.assertRaises(ValueError, Calculator.divide, 10, 0)


if __name__ == "__main__": 
    unittest.main()
