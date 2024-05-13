class BaseStats(list[int]):
    """
    A class that inherits from Python's built-in list to provide statistical
    methods on numerical lists for minimum, maximum, and range calculations.

    Methods:
    min() -> int: Returns the minimum value in the list.
    max() -> int: Returns the maximum value in the list.
    range() -> int: Returns the range of values (max-min) in the list.
    summary() -> str: Provides a formatted string of min, max, and range.
    """

    def min(self) -> int:
        """Returns the minimum value of the list."""
        return min(self)

    def max(self) -> int:
        """Returns the maximum value of the list."""
        return max(self)

    def range(self) -> int:
        """Calculates and returns the range (max-min) of the list."""
        return self.max() - self.min()

    def summary(self) -> str:
        """
        Returns a formatted string of the statistics including min, max, and range.

        Returns:
            str: A string formatted as 'min max range'.
        """
        return f"{self.min()} {self.max()} {self.range()}"
