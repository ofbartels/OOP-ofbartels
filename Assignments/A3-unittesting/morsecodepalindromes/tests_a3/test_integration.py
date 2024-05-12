import unittest
from morse_converter import MorseConverter
from palindrome_checker import PalindromeChecker


class TestMorsePalindromeIntegration(unittest.TestCase):
    """
    Integration tests for the MorseConverter and PalindromeChecker classes.
    """

    def setUp(self) -> None:
        """
        Initialize MorseConverter and PalindromeChecker for testing integration.
        """
        self.converter = MorseConverter()
        self.palindrome_checker = PalindromeChecker(self.converter)

    def test_morse_palindrome_integration_positive(self) -> None:
        """
        Test that a known palindrome phrase correctly converts to Morse code
        and is identified as a palindrome.
        """
        text = "SOS"  # SOS -> "... --- ..." which is a palindrome in Morse code.
        morse_code = self.converter.text_to_morse(text)
        result = self.palindrome_checker.is_morse_palindrome(text)
        self.assertTrue(result, f"Text '{text}' should be a Morse palindrome. Morse: {morse_code}")

    def test_morse_palindrome_integration_negative(self) -> None:
        """
        Test that a non-palindrome phrase correctly converts to Morse code
        and is identified as not a palindrome.
        """
        text = "HELLO"  # HELLO -> ".... . .-.. .-.. ---" which is not a palindrome.
        morse_code = self.converter.text_to_morse(text)
        result = self.palindrome_checker.is_morse_palindrome(text)
        self.assertFalse(result, f"Text '{text}' should not be a Morse palindrome. Morse: {morse_code}")

    def test_morse_palindrome_integration_complex(self) -> None:
        """
        Test complex phrases that are palindromes when non-alphanumeric characters are removed.
        """
        text = "Endobiotic, sanderlings, 'endobiotic"
        morse_code = self.converter.text_to_morse(text)
        result = self.palindrome_checker.is_morse_palindrome(text)
        self.assertTrue(result, f"Text '{text}' should be a Morse palindrome. Morse: {morse_code}")

    def test_empty_input(self) -> None:
        """
        Test the response to an empty input string.
        """
        text = ""
        result = self.palindrome_checker.is_morse_palindrome(text)
        self.assertFalse(result, "Empty text should not be considered a palindrome.")


if __name__ == '__main__':
    unittest.main()
