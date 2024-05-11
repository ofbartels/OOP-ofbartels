from morse_converter import MorseConverter


class PalindromeChecker:
    """
    A class to determine if the Morse code representation of a text string is a palindrome.

    Utilizes MorseConverter class to convert text to Morse code and then checks for palindrome properties.
    """

    def __init__(self, morse_converter: MorseConverter) -> None:
        """
        Initializes the PalindromeChecker with a MorseConverter object for text conversion.

        Args:
            morse_converter (MorseConverter): An instance of the MorseConverter class for converting text to Morse.
        """
        self._morse_converter = morse_converter

    @property
    def morse_converter(self) -> MorseConverter:
        """
        Provides access to the MorseConverter instance used for conversions.

        Returns:
            MorseConverter: The MorseConverter instance used for Morse code conversions.
        """
        return self._morse_converter

    @morse_converter.setter
    def morse_converter(self, value: MorseConverter) -> None:
        """
        Sets the MorseConverter instance.

        Args:
            value (MorseConverter): An instance of MorseConverter to be used for text conversions.
        """
        if not isinstance(value, MorseConverter):
            raise ValueError("morse_converter must be an instance of MorseConverter.")
        self._morse_converter = value

    def is_morse_palindrome(self, text: str) -> bool:
        """
        Determines if the Morse code representation of a given text is a palindrome.

        Args:
            text (str): The text to convert to Morse code and check for palindrome properties.

        Returns:
            bool: True if the Morse code of the text is a palindrome, False otherwise.
        """
        morse = self._morse_converter.text_to_morse(text)
        cleaned_morse = morse.replace(' ', '')  # Remove spaces for palindrome check
        if cleaned_morse == '':
            return False  # Explicitely handles empty strings
        return cleaned_morse == cleaned_morse[::-1]
