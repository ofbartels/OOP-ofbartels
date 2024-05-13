import unittest
from stats_processor import StatsProcessor
from base_stats import BaseStats


class TestStatsProcessor(unittest.TestCase):
    """Unit tests for the StatsProcessor class."""

    def setUp(self) -> None:
        """Initialize the StatsProcessor before each test."""
        self.processor = StatsProcessor()

    def tearDown(self) -> None:
        """Clean tests to ensure each test gets a fresh instance"""
        del self.processor

    def test_add_case(self) -> None:
        """Test adding a case to the processor."""
        self.processor.add_case([1, 2, 3])
        self.assertIsInstance(self.processor.cases[0], BaseStats, "The case should be an instance of BaseStats.")
        self.assertEqual(len(self.processor.cases), 1, "There should be one case in the processor.")

    def test_generate_report(self) -> None:
        """Test report generation."""
        cases = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        expected_reports = [
            "Case 1: 1 3 2",
            "Case 2: 4 6 2",
            "Case 3: 7 9 2"
        ]
        for case in cases:
            self.processor.add_case(case)
        report = self.processor.generate_report()
        self.assertEqual(report, "\n".join(expected_reports), "The generated report should match the expected output.")


if __name__ == '__main__':
    unittest.main()
