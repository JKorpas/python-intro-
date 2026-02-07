import unittest

from my_awesome_lib.basic_calculator import BasicCalculator
from parameterized import parameterized


class TestBasicCalculatorAdd(unittest.TestCase):

    def setUp(self):
        self.calc = BasicCalculator()

    @parameterized.expand(
        [
            ("both_positive", 3, 2, 5),
            ("negative/positive", -5, 3, -2),
            ("positive/negative", 5, -3, 2),
            ("both_negative", -5, -3, -8),
        ]
    )
    def test_add(self, name, x, y, result):
        self.assertEqual(self.calc.add(x, y), result)


class TestBasicCalculatorSub(unittest.TestCase):
    def setUp(self):
        self.calc = BasicCalculator()

    @parameterized.expand(
        [
            ("both_positive", 3, 2, 1),
            ("negative/positive", -3, 2, -5),
            ("positive/negative", 7, -2, 9),
            ("both_negative", -3, -3, 0),
        ]
    )
    def test_sub(self, name, x, y, result):
        self.assertEqual(self.calc.sub(x, y), result)


class TestBasicCalculatorMul(unittest.TestCase):
    def setUp(self):
        self.calc = BasicCalculator()

    @parameterized.expand([(2, 3, 6), (-4, 5, -20), (6, -3, -18), (-2, -6, 12)])
    def test_mul(self, x, y, result):
        self.assertEqual(self.calc.mul(x, y), result)


class TestBasicCalculatorDiv(unittest.TestCase):
    def setUp(self):
        self.calc = BasicCalculator()

    @parameterized.expand(
        [
            (9, 3, 3),
            (20, -5, -4),
            (-6, 1, -6),
            (-6, -2, 3),
        ]
    )
    def test_true_div(self, x, y, result):
        self.assertEqual(self.calc.div(x, y), result)

    def test_div_by_zero_should_raise(self):
        with self.assertRaises(ZeroDivisionError):
            self.calc.div(5, 0)


if __name__ == "__main__":
    unittest.main()
