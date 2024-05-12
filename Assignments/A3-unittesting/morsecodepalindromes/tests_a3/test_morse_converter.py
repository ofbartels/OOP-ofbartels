import unittest
from morse_converter import MorseConverter


class TestMorseConverter(unittest.TestCase):
    """
    Unit tests for the MorseConverter class.
    """

    def setUp(self) -> None:
        """
        Create an instance of MorseConverter that can be used in all tests.
        """
        self.converter = MorseConverter()

    def test_text_to_morse_with_alphanumeric(self) -> None:
        """
        Test converting alphanumeric text to Morse code.
        """
        text = "HELLO 123"
        expected_morse = ".... . .-.. .-.. --- .---- ..--- ...--"
        result = self.converter.text_to_morse(text)
        self.assertEqual(result, expected_morse, "Failed to convert text to Morse code.")

    def test_text_to_morse_with_non_alphanumeric(self) -> None:
        """
        Test that non-alphanumeric characters are ignored during conversion.
        """
        text = "HELLO, WORLD!"
        expected_morse = ".... . .-.. .-.. --- .-- --- .-. .-.. -.."
        result = self.converter.text_to_morse(text)
        self.assertEqual(result, expected_morse, "Non-alphanumeric characters should be ignored.")

    def test_text_to_morse_empty_string(self) -> None:
        """
        Test converting an empty string to Morse code.
        """
        text = ""
        expected_morse = ""
        result = self.converter.text_to_morse(text)
        self.assertEqual(result, expected_morse, "Empty string should return an empty Morse code.")

    def test_morse_to_text(self) -> None:
        """
        Test converting Morse code back to text.
        """
        morse = ".... . .-.. .-.. ---"
        expected_text = "HELLO"
        result = self.converter.morse_to_text(morse)
        self.assertEqual(result, expected_text, "Failed to convert Morse code back to text.")


if __name__ == '__main__':
    unittest.main()
