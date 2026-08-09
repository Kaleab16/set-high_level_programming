#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Tests for the max_integer function."""

    def test_ordered_list(self):
        """Max of an ascending list."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Max of a list in no particular order."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_descending_list(self):
        """Max of a descending list."""
        self.assertEqual(max_integer([9, 7, 5, 3]), 9)

    def test_empty_list(self):
        """Empty list returns None."""
        self.assertEqual(max_integer([]), None)

    def test_default_argument(self):
        """No argument at all uses the default empty list."""
        self.assertEqual(max_integer(), None)

    def test_single_element(self):
        """A list with only one item returns that item."""
        self.assertEqual(max_integer([42]), 42)

    def test_all_same_values(self):
        """A list where every value is identical."""
        self.assertEqual(max_integer([5, 5, 5, 5]), 5)

    def test_negative_numbers(self):
        """Max among negative numbers."""
        self.assertEqual(max_integer([-1, -5, -3]), -1)

    def test_mixed_positive_negative(self):
        """Max among a mix of positive and negative numbers."""
        self.assertEqual(max_integer([-10, 0, 10, -20]), 10)

    def test_floats(self):
        """Max works with floats too, since the function has no
        explicit int-only restriction."""
        self.assertEqual(max_integer([1.5, 2.5, 0.5]), 2.5)


if __name__ == "__main__":
    unittest.main()
