import unittest
from palindrome_checker import PalindromeChecker
from morse_converter import MorseConverter


class TestPalindromeChecker(unittest.TestCase):
    """
    Unit tests for the PalindromeChecker class.
    """

    def setUp(self) -> None:
        """
        Create an instance of MorseConverter and PalindromeChecker that can be used in all tests.
        """
        self.morse_converter = MorseConverter()
        self.palindrome_checker = PalindromeChecker(self.morse_converter)

    def test_is_morse_palindrome_true(self) -> None:
        """
        Test Morse code palindrome check with a string that is a palindrome.
        """
        text = "SOS"  # SOS in Morse is "... --- ..." which is a palindrome.
        self.assertTrue(self.palindrome_checker.is_morse_palindrome(text), "Should return True.")

    def test_is_morse_palindrome_false(self) -> None:
        """
        Test Morse code palindrome check with a string that is not a palindrome.
        """
        text = "HELLO"  # HELLO in Morse is ".... . .-.. .-.. ---" which is not a palindrome.
        self.assertFalse(self.palindrome_checker.is_morse_palindrome(text), "Should return False.")

    def test_is_morse_palindrome_with_non_alphanumeric(self) -> None:
        """
        Test Morse code palindrome check ignoring non-alphanumeric characters.
        """
        text = "IncaleScEnCe , i,'nca le scen,.ce"  # This is a classic example of a palindrome.
        self.assertTrue(self.palindrome_checker.is_morse_palindrome(text), "Should return True.")

    def test_is_morse_palindrome_empty_string(self) -> None:
        """
        Test Morse code palindrome check with an empty string.
        """
        text = ""
        self.assertFalse(self.palindrome_checker.is_morse_palindrome(text), "Should return False.")


if __name__ == '__main__':
    unittest.main()
