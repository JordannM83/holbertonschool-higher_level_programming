#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for the max_integer function."""

    def test_ordered_list(self):
        """Test an ordered list of integers."""
        pass

    def test_unordered_list(self):
        """Test an unordered list of integers."""
        pass

    def test_max_at_end(self):
        """Test a list with a beginning max value."""
        pass

    def test_max_at_beginning(self):
        """Test a list with a max value at the beginning."""
        pass

    def test_max_in_middle(self):
        """Test a list with a max value in the middle."""
        pass

    def test_one_element_list(self):
        """Test a list with a single element."""
        pass

    def test_floats(self):
        """Test a list of floats."""
        pass

    def test_ints_and_floats(self):
        """Test a list of ints and floats."""
        pass

    def test_string(self):
        """Test a string."""
        pass

    def test_list_of_strings(self):
        """Test a list of strings."""
        pass

    def test_empty_string(self):
        """Test an empty string."""
        pass

    def test_empty_list(self):
        """Test an empty list."""
        pass

    def test_none(self):
        """Test None."""
        pass


if __name__ == '__main__':
    unittest.main()
