import unittest
from sorttwonumbers import sortNumbers
from typing import Tuple


class TestSortNumbers(unittest.TestCase):
    def test_ascending_order(self) -> None:
        """
        Tests that sortNumbers correctly sorts two integers in ascending order
        when the first integer is less than the second.
        """
        result: Tuple[int, int] = sortNumbers(6, 7)
        print("Test Ascending Order: Input (6, 7), Output", result)
        self.assertEqual(result, (6, 7))

    def test_descending_order(self) -> None:
        """
        Tests that sortNumbers correctly sorts two integers in ascending order
        when the first integer is greater than the second.
        """
        result: Tuple[int, int] = sortNumbers(7, 6)
        print("Test Descending Order: Input (7, 6), Output", result)
        self.assertEqual(result, (6, 7))

    def test_equal_numbers(self) -> None:
        """
        Tests that sortNumbers correctly handles two equal integers.
        """
        result: Tuple[int, int] = sortNumbers(7, 7)
        print("Test Equal Numbers: Input (7, 7), Output", result)
        self.assertEqual(result, (7, 7))


if __name__ == '__main__':
    unittest.main()
