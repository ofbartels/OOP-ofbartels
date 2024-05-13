import unittest
from io import StringIO
from statistics import main
from unittest.mock import patch


class TestIntegration(unittest.TestCase):
    """
    Integration tests for the complete statistics application.
    Tests the application's ability to process input through to output accurately.
    """

    def test_complete_process(self) -> None:
        """
        Test the complete process from reading input to producing output.
        This simulates the user inputting data and checks the output against expected results.
        """
        test_input = """2 4 10
                        9 2 5 6 4 5 9 2 1 4
                        7 6 10 1 2 5 10 9
                        1 9"""
        expected_output = "Case 1: 4 10 6\nCase 2: 1 9 8\nCase 3: 1 10 9\nCase 4: 9 9 0\n"

        with patch('sys.stdin', new=StringIO(test_input)), patch('sys.stdout', new_callable=StringIO) as mock_output:
            main()
            self.assertEqual(mock_output.getvalue(), expected_output)

    def test_single_case(self) -> None:
        """
        Test a single case scenario to ensure the application handles small input sizes correctly.
        """
        test_input = "1 1000000"
        expected_output = "Case 1: 1000000 1000000 0\n"

        with patch('sys.stdin', new=StringIO(test_input)), patch('sys.stdout', new_callable=StringIO) as mock_output:
            main()
            self.assertEqual(mock_output.getvalue(), expected_output)


if __name__ == '__main__':
    unittest.main()
