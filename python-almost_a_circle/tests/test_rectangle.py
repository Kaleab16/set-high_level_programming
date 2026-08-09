#!/usr/bin/python3
"""Tests for the Rectangle class."""

import unittest

from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test cases for Rectangle."""

    def test_rectangle_creation(self):
        """Test rectangle creation."""
        r = Rectangle(10, 20)

        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 20)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    def test_rectangle_position(self):
        """Test x and y."""
        r = Rectangle(10, 20, 3, 4)

        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)

    def test_rectangle_id(self):
        """Test ID."""
        r = Rectangle(10, 20, id=42)

        self.assertEqual(r.id, 42)

    def test_rectangle_inheritance(self):
        """Test inheritance from Base."""
        r = Rectangle(10, 20)

        self.assertIsInstance(r, Rectangle)


if __name__ == "__main__":
    unittest.main()
