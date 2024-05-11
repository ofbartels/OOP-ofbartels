from typing import List
from point import Point


class Polygon:
    """
    Represents a convex polygon defined by a list of points in 2D space.
    """

    def __init__(self, points: List[Point]) -> None:
        """
        Initialize a new Polygon with a list of Points.

        Args:
        points (List[Point]): The vertices of the polygon in order.
        """
        self._points = points

    @property
    def points(self) -> List[Point]:
        """
        Returns the list of points forming the vertices of the polygon.
        """
        return self._points

    @points.setter
    def points(self, value: List[Point]) -> None:
        """
        Sets the list of points that form the vertices of the polygon.

        Args:
        value (List[Point]): A list of Point objects.
        """
        self._points = value

    def calculate_area(self) -> float:
        """
        Calculates and returns the area of the convex polygon using the shoelace formula.

        Returns:
        float: The area of the polygon.
        """
        n = len(self._points)  # number of vertices in the polygon
        area = 0.0
        for i in range(n):
            j = (i + 1) % n  # circular indexing
            area += self._points[i].x * self._points[j].y
            area -= self._points[j].x * self._points[i].y
        area = abs(area) / 2.0
        return area

    def __repr__(self) -> str:
        """
        Returns the string representation of the Polygon.
        """
        points_str = ', '.join(repr(p) for p in self._points)
        return f"Polygon({points_str})"
