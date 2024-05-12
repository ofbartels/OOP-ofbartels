import unittest
from unittest.mock import patch, Mock
from io import StringIO
from title_cost_calculator import TitleCostCalculator
from title_input_handler import TitleInputHandler


class TestIntegration(unittest.TestCase):
    def setUp(self) -> None:
        """Setup for each test case."""
        self.calculator = TitleCostCalculator()
        self.input_handler = TitleInputHandler(self.calculator)

    @patch('sys.stdout', new_callable=StringIO)
    def test_full_process(self, mock_stdout: Mock) -> None:
        """Test the full process from when title length is over the cap"""
        test_input = 'LongTitleName 8.5'
        expected_output = '8.5\n'  # LongTitleName is 13 characters, cap is 8.5
        self.input_handler.process_input(test_input)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_full_process_exact_length(self, mock_stdout: Mock) -> None:
        """Test the full process when title length is exactly the cap."""
        test_input = 'Seven 5'
        expected_output = '5\n'  # 'Seven' has 5 characters, cap is 5
        self.input_handler.process_input(test_input)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_full_process_under_cap(self, mock_stdout: Mock) -> None:
        """Test the full process when title length is under the cap."""
        test_input = 'Four 10'
        expected_output = '4\n'  # 'Four' has 4 characters, cap is 10
        self.input_handler.process_input(test_input)
        self.assertEqual(mock_stdout.getvalue(), expected_output)


if __name__ == '__main__':
    unittest.main()
