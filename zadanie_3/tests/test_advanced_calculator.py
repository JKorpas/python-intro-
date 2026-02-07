import unittest

from my_awesome_lib.advanced_calculator import AdvancedCalculator
from parameterized import parameterized


class TestAdvancedCalculatorFloorDiv(unittest.TestCase):
    def setUp(self):
        self.calc = AdvancedCalculator()

    @parameterized.expand([(9, 2, 4), (20, -5, -4), (-6, 2, -3), (-7, -2, 3)])
    def test_floor_div(self, x, y, result):
        self.assertEqual(self.calc.floor_div(x, y), result)

    def test_floor_div_by_zero_should_raise(self):
        self.assertRaises(ZeroDivisionError, self.calc.floor_div, 5, 0)


class TestAdvancedCalculatorPower(unittest.TestCase):
    def setUp(self):
        self.calc = AdvancedCalculator()

    @parameterized.expand([(2, 3, 8), (5, 0, 1), (-2, 3, -8), (3, 2, 9)])
    def test_power(self, x, y, result):
        self.assertEqual(self.calc.power(x, y), result)


class TestAdvancedCalculatorAbsolute(unittest.TestCase):
    def setUp(self):
        self.calc = AdvancedCalculator()

    @parameterized.expand([(5, 5), (-3, 3), (0, 0), (-100, 100)])
    def test_absolute(self, value, result):
        self.assertEqual(self.calc.absolute(value), result)


class TestAdvancedCalculatorAverage(unittest.TestCase):
    def setUp(self):
        self.calc = AdvancedCalculator()

    def test_average_list(self):
        values = [1, 2, 3, 4, 5]
        self.assertEqual(self.calc.average(values), 3)

    def test_average_empty_list_should_raise(self):
        self.assertRaises(ValueError, self.calc.average, [])


class TestAdvancedCalculatorMaxMin(unittest.TestCase):
    def setUp(self):
        self.calc = AdvancedCalculator()

    def test_maximum(self):
        values = [1, 5, 2, 10, 3]
        self.assertEqual(self.calc.maximum(values), 10)

    def test_minimum(self):
        values = [1, 5, 2, 10, 3]
        self.assertEqual(self.calc.minimum(values), 1)
