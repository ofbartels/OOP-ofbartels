from title_cost_calculator import TitleCostCalculator


class TitleInputHandler:
    """
    Handles input and output operations for the Title Cost Calculator program.
    """
    def __init__(self, calculator: TitleCostCalculator) -> None:
        """
        Initializes the TitleInputHandler with a TitleCostCalculator instance.

        Args:
            calculator (TitleCostCalculator): An instance of the TitleCostCalculator to be used for calculating the cost
        """
        self.calculator = calculator

    def parse_input(self, input_data: str) -> None:
        """
        Parses the input string to extract the title and the cap cost.

        Args:
            input_data (str): The input string containing the title and the cost cap.

        Returns:
            None
        """
        title, cap_str = input_data.rsplit(maxsplit=1)
        cap = float(cap_str)
        self.calculator.title = title
        self.calculator.cap = cap

    def format_output(self, cost: float) -> str:
        """
        Formats the calculated cost to a string with the required precision.

        Args:
            cost (float): The calculated cost to be formatted.

        Returns:
            str: The formatted cost string with dynamic precision and no trailing zeroes.
        """
        formatted_cost = f"{cost:.14f}"
        formatted_cost = formatted_cost.rstrip('0').rstrip('.')
        return formatted_cost

    def process_input(self, input_data: str) -> None:
        """
        High-level method to process the input, calculate the cost, and print the output.

        Args:
            input_data (str): The raw input data from the user or system.

        Returns:
            None
        """
        self.parse_input(input_data)
        cost = self.calculator.calculate_cost()
        formatted_output = self.format_output(cost)
        print(formatted_output)
