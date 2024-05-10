class Point:
    """
    Represents a point in 2D space.
    """

    def __init__(self, x: float, y: float) -> None:
        """
        Initialize a new Point with x and y coordinates.

        Args:
        x (float): The x-coordinate of the point.
        y (float): The y-coordinate of the point.
        """
        self._x = x
        self._y = y

    @property
    def x(self) -> float:
        """
        Returns the x-coordinate of the point.
        """
        return self._x

    @x.setter
    def x(self, value: float) -> None:
        """
        Sets the x-coordinate of the point.

        Args:
        value (float): The new x-coordinate value.
        """
        self._x = value

    @property
    def y(self) -> float:
        """
        Returns the y-coordinate of the point.
        """
        return self._y

    @y.setter
    def y(self, value: float) -> None:
        """
        Sets the y-coordinate of the point.

        Args:
        value (float): The new y-coordinate value.
        """
        self._y = value

    def __repr__(self) -> str:
        """
        Returns the string representation of the Point.
        """
        return f"Point({self.x}, {self.y})"
