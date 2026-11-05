import unittest

import circle
import square
import rectangle
import triangle


class CircleTestCase(unittest.TestCase):
    """Проверка площади круга и длины окружности."""

    def test_area(self):
        self.assertAlmostEqual(circle.area(2), 12.566370614359172)

    def test_perimeter(self):
        self.assertAlmostEqual(circle.perimeter(3), 18.84955592153876)

    def test_zero_radius(self):
        self.assertEqual(circle.area(0), 0)
        self.assertEqual(circle.perimeter(0), 0)

    def test_fractional_radius(self):
        self.assertAlmostEqual(circle.area(0.5), 0.7853981633974483)


class SquareTestCase(unittest.TestCase):
    """Проверка площади и периметра квадрата."""

    def test_area(self):
        self.assertEqual(square.area(4), 16)

    def test_perimeter(self):
        self.assertEqual(square.perimeter(5), 20)

    def test_zero_side(self):
        self.assertEqual(square.area(0), 0)
        self.assertEqual(square.perimeter(0), 0)

    def test_fractional_side(self):
        self.assertAlmostEqual(square.area(2.5), 6.25)
        self.assertAlmostEqual(square.perimeter(2.5), 10)


class RectangleTestCase(unittest.TestCase):
    """Проверка площади и периметра прямоугольника."""

    def test_area(self):
        self.assertEqual(rectangle.area(4, 5), 20)

    def test_perimeter(self):
        self.assertEqual(rectangle.perimeter(4, 5), 18)

    def test_zero_side(self):
        self.assertEqual(rectangle.area(10, 0), 0)
        self.assertEqual(rectangle.perimeter(10, 0), 20)

    def test_fractional_sides(self):
        self.assertAlmostEqual(rectangle.area(2.5, 1.5), 3.75)
        self.assertAlmostEqual(rectangle.perimeter(2.5, 1.5), 8)


class TriangleTestCase(unittest.TestCase):
    """Проверка площади и периметра треугольника."""

    def test_area(self):
        self.assertEqual(triangle.area(4, 5), 10)

    def test_perimeter(self):
        self.assertEqual(triangle.perimeter(3, 4, 5), 12)

    def test_zero_height(self):
        self.assertEqual(triangle.area(4, 0), 0)

    def test_fractional_values(self):
        self.assertAlmostEqual(triangle.area(2.5, 1.5), 1.875)
        self.assertAlmostEqual(triangle.perimeter(2.5, 3.5, 4.5), 10.5)


if __name__ == "__main__":
    unittest.main()
