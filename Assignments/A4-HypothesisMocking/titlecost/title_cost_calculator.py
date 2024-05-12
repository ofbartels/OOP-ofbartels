class TitleCostCalculator:
    """
    Calculator for determining the cost of transmitting a movie title based on its length and a provided cap.
    """
    def __init__(self, title: str = "", cap: float = 0.0) -> None:
        """
        Initializes a new instance of the TitleCostCalculator with an optional title and cap.

        Args:
            title (str): The title of the movie.
            cap (float): The cap on the cost.
        """
        self._title = title
        self._cap = cap

    @property
    def title(self) -> str:
        """
        Gets the movie title.

        Returns:
            str: The movie title.
        """
        return self._title

    @title.setter
    def title(self, value: str) -> None:
        """
        Sets the movie title.

        Args:
            value (str): The new title to be set.
        """
        self._title = value

    @property
    def cap(self) -> float:
        """
        Gets the cost cap.

        Returns:
            float: The cost cap.
        """
        return self._cap

    @cap.setter
    def cap(self, value: float) -> None:
        """
        Sets the cost cap.

        Args:
            value (float): The new cost cap to be set.
        """
        self._cap = value

    def calculate_cost(self) -> float:
        """
        Calculates the transmission cost of the movie title.

        Returns:
            float: The lesser of the title length or the cost cap.
        """
        return min(len(self._title), self._cap)
