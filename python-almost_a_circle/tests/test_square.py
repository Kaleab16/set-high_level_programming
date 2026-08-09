#!/usr/bin/python3
"""Tests for the Square class."""

import unittest

from models.square import Square


class TestSquare(unittest.TestCase):
    """Test cases for Square."""

    def test_square_creation(self):
        """Test square creation."""
        s = Square(10)

        self.assertEqual(s.width, 10)
        self.assertEqual(s.height, 10)

    def test_square_position(self):
        """Test x and y."""
        s = Square(10, 3, 4)

        self.assertEqual(s.x, 3)
        self.assertEqual(s.y, 4)

    def test_square_id(self):
        """Test ID."""
        s = Square(10, id=42)

        self.assertEqual(s.id, 42)

    def test_square_inheritance(self):
        """Test inheritance."""
        s = Square(10)

        self.assertIsInstance(s, Square)


if __name__ == "__main__":
    unittest.main()
