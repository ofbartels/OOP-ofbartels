import unittest
from unittest.mock import patch
from io import StringIO
from title_cost_calculator import TitleCostCalculator
from title_input_handler import TitleInputHandler


class TestTitleInputHandler(unittest.TestCase):
    def setUp(self) -> None:
        # Setup a TitleCostCalculator instance for use in tests
        self.calculator = TitleCostCalculator()
        self.handler = TitleInputHandler(self.calculator)

    def test_parse_input_basic(self) -> None:
        """Test parsing of basic input."""
        input_data = "MovieTitle 10.0"
        self.handler.parse_input(input_data)
        self.assertEqual(self.calculator.title, "MovieTitle")
        self.assertEqual(self.calculator.cap, 10.0)

    def test_parse_input_with_cap_at_boundary(self) -> None:
        """Test parsing input where the cap is at a typical boundary value."""
        input_data = "BoundaryCase 5.5"
        self.handler.parse_input(input_data)
        self.assertEqual(self.calculator.title, "BoundaryCase")
        self.assertEqual(self.calculator.cap, 5.5)

    def test_format_output_precise(self) -> None:
        """Test that the output is formatted to the specified precision without unnecessary trailing zeros."""
        # Set arbitrary values to test output formatting
        self.calculator.title = "PreciseTitle"
        self.calculator.cap = 8.123456789
        calculated_cost = 8.12345678  # Simulate a calculated cost very close to cap
        formatted_output = self.handler.format_output(calculated_cost)
        self.assertEqual(formatted_output, "8.12345678")

    def test_format_output_no_trailing_zeroes(self) -> None:
        """Ensure no unnecessary trailing zeros are in the formatted output."""
        self.calculator.title = "ShortTitle"
        self.calculator.cap = 3.0
        calculated_cost = 3.0  # This should not display as 3.00000000
        formatted_output = self.handler.format_output(calculated_cost)
        self.assertEqual(formatted_output, "3")

    def test_process_input_integration(self) -> None:
        """Test the full process from input to formatted output."""
        input_data = "ExampleMovie 12.345"
        expected_output = "12\n"  # ExampleMovie has 12 characters, cap is 12.345, expecting newline in output
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.handler.process_input(input_data)
            # The output is captured from stdout
            self.assertEqual(mock_stdout.getvalue(), expected_output)


if __name__ == '__main__':
    unittest.main()
