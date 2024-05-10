import unittest
from point import Point
from polygon import Polygon
from convexpolygonarea import parse_input, main
from io import StringIO
import sys


class TestPoint(unittest.TestCase):
    def test_point_creation(self):
        pt = Point(1, 2)
        self.assertEqual(pt.x, 1)
        self.assertEqual(pt.y, 2)

    def test_point_repr(self):
        pt = Point(3, 4)
        self.assertEqual(repr(pt), "Point(3, 4)")


class TestPolygon(unittest.TestCase):
    def setUp(self):
        self.points = [Point(0, 0), Point(4, 0), Point(4, 3), Point(0, 3)]
        self.poly = Polygon(self.points)

    def test_polygon_creation(self):
        self.assertEqual(len(self.poly.points), 4)
        self.assertIsInstance(self.poly.points[0], Point)

    def test_area_calculation(self):
        # Rectangle with known area of 12
        self.assertEqual(self.poly.calculate_area(), 12)

    def test_polygon_repr(self):
        repr_str = "Polygon(Point(0, 0), Point(4, 0), Point(4, 3), Point(0, 3))"
        self.assertEqual(repr(self.poly), repr_str)


class TestConvexPolygonArea(unittest.TestCase):
    def test_input_parsing(self):
        # Redirect standard input for the duration of the test
        test_input = "1\n3 0 0 4 0 4 3\n"
        sys.stdin = StringIO(test_input)
        polygons = parse_input()
        sys.stdin = sys.__stdin__  # Reset standard input
        self.assertEqual(len(polygons), 1)
        self.assertEqual(polygons[0].calculate_area(), 6.0)

    def test_main_output(self):
        # Redirect standard output for the duration of the test
        test_input = "2\n3 1 1 2 1 1 5\n4 0 0 4 0 4 3 0 3\n"
        sys.stdin = StringIO(test_input)
        sys.stdout = StringIO()
        main()
        output = sys.stdout.getvalue()
        sys.stdout = sys.__stdout__  # Reset standard output
        expected_output = "0.5\n12\n"
        self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main()
