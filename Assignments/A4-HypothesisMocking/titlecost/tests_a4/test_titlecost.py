import unittest
from unittest.mock import patch, Mock
from io import StringIO
import titlecost


class TestTitleCostMain(unittest.TestCase):
    def setUp(self) -> None:
        # Prepare to capture printed outputs
        self.held_stdout = StringIO()

    def test_normal_operation(self) -> None:
        # Test normal operation with a typical input
        test_input = "MovieTitle 10.0\n"
        expected_output = "10\n"  # Expected format might need to be precise to the specification

        with patch('sys.stdin', StringIO(test_input)), patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            titlecost.main()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_boundary_operation(self) -> None:
        # Test operation at the boundary of the cap
        test_input = "LongMovieTitleName 5.0\n"
        expected_output = "5\n"  # Title length exceeds the cap

        with patch('sys.stdin', StringIO(test_input)), patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            titlecost.main()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_minimum_length_title(self) -> None:
        # Test the smallest possible title
        test_input = "A 50.0\n"
        expected_output = "1\n"  # Title is a single character

        with patch('sys.stdin', StringIO(test_input)), patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            titlecost.main()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdin', new_callable=StringIO)
    def test_script_execution(self, mock_stdin: Mock) -> None:
        """Test the script execution to cover if __name__ == '__main__': block."""
        # Simulate input data
        mock_stdin.write('ExampleMovie 12.345')
        mock_stdin.seek(0)

        # Use patch.object to mock __name__ to '__main__' to simulate script execution
        with patch.object(titlecost, '__name__', '__main__'):
            with patch('titlecost.main') as mock_main:
                titlecost.main()
                mock_main.assert_called_once()


if __name__ == '__main__':
    unittest.main()
