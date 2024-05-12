import sys
from title_cost_calculator import TitleCostCalculator
from title_input_handler import TitleInputHandler


def main() -> None:
    input_data = sys.stdin.read().strip()
    calculator = TitleCostCalculator()
    input_handler = TitleInputHandler(calculator)
    input_handler.process_input(input_data)


if __name__ == "__main__":
    main()
