#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Define unittests for max_integer function."""

    def test_ordered_list(self):
        """Test with an ordered list of integers."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test with an unordered list of integers."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        """Test with the max integer at the beginning."""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_empty_list(self):
        """Test with an empty list."""
        self.assertEqual(max_integer([]), None)

    def test_one_element(self):
        """Test with a list of one element."""
        self.assertEqual(max_integer([7]), 7)

    def test_only_negative(self):
        """Test with a list of only negative numbers."""
        self.assertEqual(max_integer([-1, -5, -3, -4]), -1)

    def test_mixed_numbers(self):
        """Test with a mixed list of positive and negative numbers."""
        self.assertEqual(max_integer([-1, 2, 3, -4]), 3)

    def test_duplicate_numbers(self):
        """Test with duplicate numbers in the list."""
        self.assertEqual(max_integer([4, 4, 2, 1]), 4)


if __name__ == '__main__':
    unittest.main()
