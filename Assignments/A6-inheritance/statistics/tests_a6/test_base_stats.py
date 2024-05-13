import unittest
from hypothesis import given, strategies as st
from base_stats import BaseStats
from typing import List


class TestBaseStats(unittest.TestCase):
    """Unit tests for the BaseStats class."""

    @given(st.lists(st.integers(min_value=-1000000, max_value=1000000), min_size=1))
    def test_min(self, lst: List[int]) -> None:
        """Test that the minimum value is calculated correctly."""
        stats = BaseStats(lst)
        expected_min = min(lst)
        self.assertEqual(stats.min(), expected_min, f"Expected minimum of {expected_min} but got {stats.min()}.")

    @given(st.lists(st.integers(min_value=-1000000, max_value=1000000), min_size=1))
    def test_max(self, lst: List[int]) -> None:
        """Test that the maximum value is calculated correctly."""
        stats = BaseStats(lst)
        expected_max = max(lst)
        self.assertEqual(stats.max(), expected_max, f"Expected maximum of {expected_max} but got {stats.max()}.")

    @given(st.lists(st.integers(min_value=-1000000, max_value=1000000), min_size=1))
    def test_range(self, lst: List[int]) -> None:
        """Test that the range is calculated correctly."""
        stats = BaseStats(lst)
        expected_range = max(lst) - min(lst)
        self.assertEqual(stats.range(), expected_range, f"Expected range of {expected_range} but got {stats.range()}.")

    def test_summary(self) -> None:
        """Test the summary method outputs the correct format."""
        stats = BaseStats([1, 2, 3, 4, 5])
        expected_sum = "1 5 4"
        self.assertEqual(stats.summary(), expected_sum, f"Expected '{expected_sum}' but got '{stats.summary()}'.")


if __name__ == '__main__':
    unittest.main()
