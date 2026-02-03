import unittest

from app import area, check_email, is_palindrome, sort_numbers
from parameterized import parameterized


def setUpModule():
    print("Setting up module...")


def tearDownModule():
    print("Tearing down module...")


class TestArea(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print(f"Setting up class: {cls.__name__}")

    @classmethod
    def tearDownClass(cls):
        print(f"Tearing down class: {cls.__name__}")

    def setUp(self):
        print("setting up")

    def tearDown(self):
        print("tearing down")

    def test_area(self):
        self.assertEqual(area(4, 5), 20)

    @parameterized.expand([(1, 2, 2), (2, 3, 6), (5.5, 2, 11.0), (1, 8, 8)])
    def test_area_correct_values(self, width, height, expected):
        self.assertEqual(area(width, height), expected)

    def test_area_incorrect_type_Should_raise_error(self):
        self.assertRaises(TypeError, area, "4", 5)
        self.assertRaises(TypeError, area, 4, "5")

    def test_area_negative_value_Should_raise_error(self):
        self.assertRaises(ValueError, area, -4, 5)
        self.assertRaises(ValueError, area, 4, -5)


class TestEmailValidation(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print(f"Setting up class: {cls.__name__}")

    @classmethod
    def tearDownClass(cls):
        print(f"Tearing down class: {cls.__name__}")

    def setUp(self):
        print("setting up")

    def tearDown(self):
        print("tearing down")

    def test_email_is_string(self):
        self.assertTrue(isinstance("user@mail.com", str))

    def test_valid_email(self):
        self.assertTrue(check_email("user@mail.com"))

    def test_email_is_not_string(self):
        self.assertFalse(check_email(123))

    def test_email_missing_at_symbol(self):
        self.assertFalse(check_email("usermail.com"))


class TestSortListNumbers(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print(f"Setting up class: {cls.__name__}")

    @classmethod
    def tearDownClass(cls):
        print(f"Tearing down class: {cls.__name__}")

    def setUp(self):
        print("setting up")

    def tearDown(self):
        print("tearing down")

    def test_sort_correct_list(self):
        self.assertEqual(sort_numbers([2, 1, 9, 0, 7, 5, 12]), [0, 1, 2, 5, 7, 9, 12])

    def test_sort_floats(self):
        self.assertEqual(
            sort_numbers([5.5, 1.7, 3.2, 8.8, 4.1]), [1.7, 3.2, 4.1, 5.5, 8.8]
        )

    def test_non_numeric_elements_Should_raise(self):
        self.assertRaises(TypeError, sort_numbers, [1, "two", 3])


class TestIsPalindrome(unittest.TestCase):

    def test_simple_palindrome(self):
        self.assertTrue(is_palindrome("kajak"))

    def test_not_palindrome(self):
        self.assertFalse(is_palindrome("Programowanie zaawansowane"))

    def test_complex_palindrome(self):
        self.assertTrue(is_palindrome("Kobyła ma mały bok"))

    def test_non_string_input_should_raise(self):
        self.assertRaises(TypeError, is_palindrome, 123123)


if __name__ == "__main__":
    unittest.main()
