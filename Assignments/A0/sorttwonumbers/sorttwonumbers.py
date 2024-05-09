from typing import Tuple

def sortNumbers(num1: int, num2: int) -> Tuple[int, int]:
    """
    Sorts two numbers in ascending order.

    Args:
    num1 (int): The first number.
    num2 (int): The second number.

    Returns:
    Tuple[int, int]: A tuple containing the sorted numbers.
    """
    if num1 <= num2:
        return num1, num2
    else:
        return num2, num1

# Main execution block
if __name__ == "__main__":
    try:
        line = input("Enter two integers separated by space: ")
        a, b = map(int, line.split())
        sorted_nums = sortNumbers(a, b)
        print(f"{sorted_nums[0]} {sorted_nums[1]}")
    except ValueError:
        print("Please enter valid integers.")