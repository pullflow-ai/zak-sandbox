import unittest

# Import the calculate function from calc.py
from calc import calculate

class TestCalculateFunction(unittest.TestCase):
    
    def test_basic_addition(self):
        self.assertEqual(calculate("1 + 1"), 2.0)
    
    def test_basic_subtraction(self):
        self.assertEqual(calculate("5 - 3"), 2.0)
    
    def test_basic_multiplication(self):
        self.assertEqual(calculate("4 * 2"), 8.0)
    
    def test_basic_division(self):
        self.assertEqual(calculate("8 / 2"), 4.0)
    
    def test_combined_operations(self):
        self.assertEqual(calculate("2 + 3 * 4"), 14.0)
    
    def test_parentheses_operations(self):
        self.assertEqual(calculate("(2 + 3) * 4"), 20.0)
    
    def test_nested_parentheses(self):
        self.assertEqual(calculate("((1 + 2) * (3 + 4)) / 2"), 10.5)
    
    def test_whitespace_handling(self):
        self.assertEqual(calculate(" 12 +  2 *  3 "), 18.0)
    
    def test_float_handling(self):
        self.assertEqual(calculate("3.5 + 2.1"), 5.6)
    
    def test_expression_with_parentheses(self):
        self.assertEqual(calculate("(12 + 2) * 2 + 15"), 43.0)
    
    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            calculate("5 / 0")
    
    def test_invalid_expression(self):
        with self.assertRaises(IndexError):
            calculate("(5 + 3))")  # Unmatched parentheses

if __name__ == '__main__':
    unittest.main()