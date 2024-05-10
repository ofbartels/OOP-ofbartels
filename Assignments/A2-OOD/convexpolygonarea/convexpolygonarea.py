from typing import List
from polygon import Polygon
from point import Point


def parse_input() -> List[Polygon]:
    """
    Parses input from standard input according to the Kattis problem format.

    Returns:
    List[Polygon]: A list of Polygon objects constructed from the input data.
    """
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    polygons = []

    for line in data[1:]:
        if line.strip():
            parts = list(map(float, line.split()))
            points = [Point(parts[i], parts[i+1]) for i in range(1, len(parts), 2)]
            polygon = Polygon(points)
            polygons.append(polygon)

    return polygons


def main():
    """
    Main function to read, process, and output the area of each convex polygon.
    """
    polygons = parse_input()
    for polygon in polygons:
        area = polygon.calculate_area()
        if area.is_integer():
            print(f"{int(area)}")
        else:
            print(f"{area:.1f}")


if __name__ == '__main__':
    main()
