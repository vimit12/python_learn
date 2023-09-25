import unittest

# The class containing the functions or methods to be tested
class MyFunctions:
    def add(self, a, b):
        return a + b

    def multiply(self, a, b):
        return a * b

# The test class that inherits from unittest.TestCase
class TestMyFunctions(unittest.TestCase):
    # Test case for the add() function
    def test_add(self):
        my_func = MyFunctions()
        result = my_func.add(2, 3)
        self.assertEqual(result, 5)  # Assertion to check if the result is as expected

    # Test case for the multiply() function
    def test_multiply(self):
        my_func = MyFunctions()
        result = my_func.multiply(2, 3)
        self.assertEqual(result, 6)  # Assertion to check if the result is as expected

# Running the tests
if __name__ == '__main__':
    unittest.main()
