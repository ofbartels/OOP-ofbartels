import unittest
from sorttwonumbers import sortNumbers

class TestSortNumbers(unittest.TestCase):
    
    def test_ascending_order(self):
        result = sortNumbers(6, 7)
        print("Test Ascending Order: Input (6, 7), Output", result)
        self.assertEqual(result, (6, 7))

    def test_descending_order(self):
        result = sortNumbers(7, 6)
        print("Test Descending Order: Input (7, 6), Output", result)
        self.assertEqual(result, (6, 7))

    def test_equal_numbers(self):
        result = sortNumbers(7, 7)
        print("Test Equal Numbers: Input (7, 7), Output", result)
        self.assertEqual(result, (7, 7))

if __name__ == '__main__':
    unittest.main()