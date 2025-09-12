#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for the max_integer function."""

    def test_ordered_list(self):
        """Test an ordered list of integers."""
        max_integer([1, 2, 3, 4, 5])

    def test_unordered_list(self):
        """Test an unordered list of integers."""
        max_integer([3, 4, 1, 5, 2])

    def test_max_at_end(self):
        """Test a list with a beginning max value."""
        max_integer([3, 4, 2, 1, 5])

    def test_max_at_beginning(self):
        """Test a list with a max value at the beginning."""
        max_integer([6, 2, 3, 1, 4, 5])

    def test_max_in_middle(self):
        """Test a list with a max value in the middle."""
        max_integer([1, 2, 5, 3, 4])

    def test_one_element_list(self):
        """Test a list with a single element."""
        max_integer([5])

    def test_floats(self):
        """Test a list of floats."""
        max_integer([1.5, 1.2, 1.3, 1.6, 1.4])

    def test_ints_and_floats(self):
        """Test a list of ints and floats."""
        max_integer([1, 1.5, 3, 4, 4.5])

    def test_string(self):
        """Test a string."""
        max_integer(["hello"])

    def test_list_of_strings(self):
        """Test a list of strings."""
        max_integer(["hello", "world", "!!!"])

    def test_empty_string(self):
        """Test an empty string."""
        max_integer([""])

    def test_empty_list(self):
        """Test an empty list."""
        max_integer([])

    def test_none(self):
        """Test None."""
        max_integer()


if __name__ == '__main__':
    unittest.main()
