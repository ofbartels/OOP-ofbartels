import sys
from morse_converter import MorseConverter
from palindrome_checker import PalindromeChecker


def main() -> None:
    """
    Main function that reads input, checks if it is a Morse code palindrome, and outputs the result.

    It reads a single line of input, uses MorseCode to convert it to Morse code,
    and then uses PalindromeChecker to check if the converted Morse code is a palindrome.
    Outputs 1 if true, otherwise 0.
    """
    input_text = sys.stdin.read().strip()  # Reading input from standard input (typically for Kattis problems)

    morse_converter = MorseConverter()  # Create a MorseConverter object for conversions
    checker = PalindromeChecker(morse_converter)  # Create a PalindromeChecker object to check for palindromes

    # Determine if the input text, when converted to Morse code, is a palindrome
    result = 1 if checker.is_morse_palindrome(input_text) else 0

    print(result)  # Print the result as required by Kattis


if __name__ == "__main__":
    main()
