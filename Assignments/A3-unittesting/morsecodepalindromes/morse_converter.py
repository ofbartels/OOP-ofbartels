class MorseConverter:
    """
    A class to handle operations related to Morse code conversions.

    Attributes:
        _morse_dict (dict): A private dictionary mapping characters to Morse code.
    """

    def __init__(self) -> None:
        """
        Initializes the MorseCode with a dictionary for Morse code conversions.
        """
        self._morse_dict: dict[str, str] = {
            'A': '.-',    'B': '-...',  'C': '-.-.',  'D': '-..',
            'E': '.',     'F': '..-.',  'G': '--.',   'H': '....',
            'I': '..',    'J': '.---',  'K': '-.-',   'L': '.-..',
            'M': '--',    'N': '-.',    'O': '---',   'P': '.--.',
            'Q': '--.-',  'R': '.-.',   'S': '...',   'T': '-',
            'U': '..-',   'V': '...-',  'W': '.--',   'X': '-..-',
            'Y': '-.--',  'Z': '--..',  '0': '-----', '1': '.----',
            '2': '..---', '3': '...--', '4': '....-', '5': '.....',
            '6': '-....', '7': '--...', '8': '---..', '9': '----.'
        }

    @property
    def morse_dict(self) -> dict[str, str]:
        """
        Returns a copy of the Morse code dictionary to ensure encapsulation.

        Returns:
            dict: A copy of the Morse code dictionary.
        """
        return self._morse_dict.copy()

    @morse_dict.setter
    def morse_dict(self, value: dict[str, str]) -> None:
        """
        Sets the Morse code dictionary.

        Args:
            value (dict): A dictionary mapping characters to Morse code.
        """
        if not isinstance(value, dict):
            raise ValueError("Morse dictionary must be a dictionary.")
        self._morse_dict = value

    def text_to_morse(self, text: str) -> str:
        """
        Converts text to Morse code using the Morse dictionary ignoring non-alphanumeric characters.

        Args:
            text (str): The text to convert to Morse code.

        Returns:
            str: The Morse code string corresponding to the input text.
        """
        return ' '.join(self._morse_dict[char] for char in text.upper() if char.isalnum() and char in self._morse_dict)

    def morse_to_text(self, morse: str) -> str:
        """
        Converts Morse code to text by reversing the Morse dictionary.

        Args:
            morse (str): The Morse code string to convert to text.

        Returns:
            str: The text string corresponding to the input Morse code.
        """
        inverse_dict = {v: k for k, v in self._morse_dict.items()}
        return ''.join(inverse_dict[code] for code in morse.split() if code in inverse_dict)
