import unittest
from unittest.mock import patch, MagicMock
from io import StringIO
from statistics import main


class TestStatistics(unittest.TestCase):
    """
    Unit tests for the statistics.py main module.
    """

    @patch('statistics.StatsProcessor')
    @patch('sys.stdin', new_callable=lambda: StringIO('2 4 10\n1 9'))
    @patch('sys.stdout', new_callable=StringIO)
    def test_main_execution(self, mock_stdout: StringIO, mock_stdin: StringIO, mock_stats_processor: MagicMock) -> None:
        """
        Test the main function to ensure it correctly initializes the processor,
        processes input, and outputs the expected results.
        """
        # Setup a mock for StatsProcessor to return a specific result
        mock_processor_instance = mock_stats_processor.return_value
        mock_processor_instance.generate_report.return_value = "Case 1: 4 10 6"

        # Call the main function
        main()

        # Assert that StatsProcessor was initialized and used correctly
        mock_stats_processor.assert_called_once()
        mock_processor_instance.process_input.assert_called_once_with(['2 4 10', '1 9'])
        mock_processor_instance.generate_report.assert_called_once()

        # Assert the output is as expected
        self.assertEqual(mock_stdout.getvalue(), "Case 1: 4 10 6\n")

    def test_main_no_input(self) -> None:
        """
        Test the main function with no input to ensure it handles empty scenarios gracefully.
        """
        with patch('sys.stdin', new=StringIO('')), \
             patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            main()
            # Expect no output when there is no input
            self.assertEqual(mock_stdout.getvalue(), '\n')


if __name__ == '__main__':
    unittest.main()
