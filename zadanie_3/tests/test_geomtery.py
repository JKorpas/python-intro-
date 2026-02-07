import unittest

from my_awesome_lib.geometry import Geometry
from parameterized import parameterized


class TestRectangle(unittest.TestCase):

    def setUp(self):
        self.geo = Geometry()

    @parameterized.expand(
        [
            (4, 5, 20),
            (2.5, 4, 10),
        ]
    )
    def test_rectangle_area(self, width, height, result):
        self.assertEqual(self.geo.rectangle_area(width, height), result)

    @parameterized.expand(
        [
            (4, 5, 18),
            (2, 3, 10),
        ]
    )
    def test_rectangle_perimeter(self, width, height, result):
        self.assertEqual(self.geo.rectangle_perimeter(width, height), result)

    def test_rectangle_negative_value_should_raise(self):
        self.assertRaises(ValueError, self.geo.rectangle_area, -2, 5)

    def test_rectangle_wrong_type_should_raise(self):
        self.assertRaises(TypeError, self.geo.rectangle_area, "4", 5)


class TestSquare(unittest.TestCase):

    def setUp(self):
        self.geo = Geometry()

    @parameterized.expand(
        [
            (4, 16),
            (2.5, 6.25),
        ]
    )
    def test_square_area(self, side, result):
        self.assertEqual(self.geo.square_area(side), result)

    @parameterized.expand(
        [
            (4, 16),
            (3, 12),
        ]
    )
    def test_square_perimeter(self, side, result):
        self.assertEqual(self.geo.square_perimeter(side), result)

    def test_square_zero_should_raise(self):
        self.assertRaises(ValueError, self.geo.square_area, 0)


class TestCircle(unittest.TestCase):

    def setUp(self):
        self.geo = Geometry()

    def test_circle_area(self):
        self.assertAlmostEqual(self.geo.circle_area(1), 3.14, places=2)

    def test_circle_circumference(self):
        self.assertAlmostEqual(self.geo.circle_circumference(1), 6.28, places=2)

    def test_circle_negative_radius_should_raise(self):
        self.assertRaises(ValueError, self.geo.circle_area, -1)


class TestTriangle(unittest.TestCase):

    def setUp(self):
        self.geo = Geometry()

    def test_triangle_area(self):
        self.assertEqual(self.geo.triangle_area(4, 5), 10)

    def test_triangle_perimeter(self):
        self.assertEqual(self.geo.triangle_perimeter(3, 4, 5), 12)

    def test_triangle_wrong_type_should_raise(self):
        self.assertRaises(TypeError, self.geo.triangle_perimeter, 3, "4", 5)


if __name__ == "__main__":
    unittest.main()
