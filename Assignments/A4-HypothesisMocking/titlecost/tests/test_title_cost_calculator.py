import unittest
from title_cost_calculator import TitleCostCalculator


class TestTitleCostCalculator(unittest.TestCase):
    def test_cost_calculation_exact_cap(self) -> None:
        """Test cost calculation when the title length is exactly the cap."""
        calculator = TitleCostCalculator(title="TwelveBabies", cap=12.0)
        self.assertEqual(calculator.calculate_cost(), 12.0)

    def test_cost_calculation_below_cap(self) -> None:
        """Test cost calculation when the title length is below the cap."""
        calculator = TitleCostCalculator(title="Short", cap=10.0)
        self.assertEqual(calculator.calculate_cost(), 5.0)  # 'Short' has 5 characters

    def test_cost_calculation_above_cap(self) -> None:
        """Test cost calculation when the title length exceeds the cap."""
        calculator = TitleCostCalculator(title="VeryLongTitleName", cap=5.0)
        self.assertEqual(calculator.calculate_cost(), 5.0)  # Cap is 5, title is longer

    def test_cost_calculation_with_no_title(self) -> None:
        """Test cost calculation with an empty title and a non-zero cap."""
        calculator = TitleCostCalculator(title="", cap=10.0)
        self.assertEqual(calculator.calculate_cost(), 0.0)  # No title, cost should be 0

    def test_cost_calculation_with_no_cap(self) -> None:
        """Test cost calculation with a normal title but a cap of zero."""
        calculator = TitleCostCalculator(title="Normal", cap=0.0)
        self.assertEqual(calculator.calculate_cost(), 0.0)  # Cap is 0, cost should be 0 despite the title length

    def test_cost_calculation_float_precision(self) -> None:
        """Test cost calculation ensuring float precision issues are handled."""
        calculator = TitleCostCalculator(title="ElevenChars", cap=11.000000001)
        self.assertAlmostEqual(calculator.calculate_cost(), 11.0, places=8)  # Testing floating-point precision


if __name__ == '__main__':
    unittest.main()
