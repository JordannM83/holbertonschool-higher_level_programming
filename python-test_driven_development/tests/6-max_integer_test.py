#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for the max_integer function."""

    def test_ordered_list(self):
        """Test an ordered list of integers."""
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)

    def test_unordered_list(self):
        """Test an unordered list of integers."""
        self.assertEqual(max_integer([3, 4, 1, 5, 2]), 5)

    def test_max_at_end(self):
        """Test a list with a beginning max value."""
        self.assertEqual(max_integer([3, 4, 2, 1, 5]), 5)

    def test_max_at_beginning(self):
        """Test a list with a max value at the beginning."""
        self.assertEqual(max_integer([6, 2, 3, 1, 4, 5]), 6)

    def test_max_in_middle(self):
        """Test a list with a max value in the middle."""
        self.assertEqual(max_integer([1, 2, 5, 3, 4]), 5)

    def test_one_element_list(self):
        """Test a list with a single element."""
        self.assertEqual(max_integer([5]), 5)

    def test_floats(self):
        """Test a list of floats."""
        self.assertEqual(max_integer([1.5, 1.2, 1.3, 1.6, 1.4]), 1.6)

    def test_ints_and_floats(self):
        """Test a list of ints and floats."""
        self.assertEqual(max_integer([1, 1.5, 3, 4, 4.5]), 4.5)

    def test_string(self):
        """Test a string."""
        self.assertEqual(max_integer(["hello"]), "hello")

    def test_list_of_strings(self):
        """Test a list of strings."""
        self.assertEqual(max_integer(["hello", "world", "!!!"]), "world")

    def test_empty_string(self):
        """Test an empty string."""
        self.assertEqual(max_integer([""]), "")

    def test_empty_list(self):
        """Test an empty list."""
        self.assertIsNone(max_integer([]))

    def test_none(self):
        """Test None."""
        self.assertIsNone(max_integer())

    def test_negative_numbers(self):
        """Test a list of negative numbers."""
        self.assertEqual(max_integer([-1, -2, -3, -4, -5]), -1)

    def test_positive_and_negative(self):
        """Test a list with positive and negative numbers."""
        self.assertEqual(max_integer([-10, -5, 0, 5, 10]), 10)

    def test_all_same_numbers(self):
        """Test a list where all numbers are the same."""
        self.assertEqual(max_integer([7, 7, 7, 7]), 7)

    def test_large_numbers(self):
        """Test a list with large numbers."""
        self.assertEqual(max_integer([1000000, 999999, 1000001]), 1000001)

    def test_zero_in_list(self):
        """Test a list containing zero."""
        self.assertEqual(max_integer([0, -1, -2]), 0)


if __name__ == '__main__':
    unittest.main()
