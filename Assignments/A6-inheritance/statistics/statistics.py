import sys
from stats_processor import StatsProcessor


def main() -> None:
    """
    Main function to handle the flow of processing statistics from input.
    Reads from standard input, processes the data, and prints out the results.
    """
    processor = StatsProcessor()
    input_data = sys.stdin.read().strip().split("\n")
    processor.process_input(input_data)
    result = processor.generate_report()
    print(result)


if __name__ == "__main__":
    main()
