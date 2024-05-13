from base_stats import BaseStats
from typing import List


class StatsProcessor:
    """
    Processes multiple data samples and calculates statistical properties
    using instances of the BaseStats class.

    Attributes:
        cases (list of BaseStats): A list to hold multiple instances of BaseStats.

    Methods:
        add_case(data: list): Adds a new BaseStats instance to the cases.
        process_input(input_lines: list): Parses raw input lines and extracts data samples.
        generate_report() -> str: Generates a formatted report of statistics for all cases.
    """

    def __init__(self) -> None:
        """Initialize the StatsProcessor with an empty list of cases."""
        self.cases: List[BaseStats] = []

    def add_case(self, data: List[int]) -> None:
        """
        Adds a new case with given data to the processor for statistical analysis.

        Args:
            data (list): A list of integers representing the data for one case.
        """
        stats = BaseStats(data)
        self.cases.append(stats)

    def process_input(self, input_lines: List[str]) -> None:
        """
        Processes raw input lines to extract cases and populate them into BaseStats instances.

        Args:
            input_lines (list): A list of strings, each representing one line of input.
        """
        for line in input_lines:
            parts = list(map(int, line.split()))
            if len(parts) > 1:
                n = parts[0]
                if n < len(parts) - 1:
                    values = parts[1:n+1]
                else:
                    values = parts[1:]
                self.add_case(values)
            elif len(parts) == 1:
                pass

    def generate_report(self) -> str:
        """
        Generates a formatted report for all cases, showing the case number and its statistics.

        Returns:
            str: A string containing the formatted report for all cases.
        """
        report_lines = []
        for index, case in enumerate(self.cases, start=1):
            report_lines.append(f"Case {index}: {case.summary()}")
        return "\n".join(report_lines)
