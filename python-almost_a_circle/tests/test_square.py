#!/usr/bin/python3
"""Unittest for the Square class."""
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """Tests for Square."""

    def test_basic_creation(self):
        """A basic Square(1) is created without error."""
        s = Square(1)
        self.assertEqual(s.width, 1)
        self.assertEqual(s.height, 1)

    def test_with_x(self):
        """Square(1, 2) sets x."""
        s = Square(1, 2)
        self.assertEqual(s.x, 2)

    def test_with_x_and_y(self):
        """Square(1, 2, 3) sets x and y."""
        s = Square(1, 2, 3)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)

    def test_size_not_int(self):
        """A non-integer size raises TypeError."""
        with self.assertRaises(TypeError):
            Square("1")

    def test_x_not_int(self):
        """A non-integer x raises TypeError."""
        with self.assertRaises(TypeError):
            Square(1, "2")

    def test_y_not_int(self):
        """A non-integer y raises TypeError."""
        with self.assertRaises(TypeError):
            Square(1, 2, "3")

    def test_size_negative(self):
        """A negative size raises ValueError."""
        with self.assertRaises(ValueError):
            Square(-1)

    def test_x_negative(self):
        """A negative x raises ValueError."""
        with self.assertRaises(ValueError):
            Square(1, -2)

    def test_y_negative(self):
        """A negative y raises ValueError."""
        with self.assertRaises(ValueError):
            Square(1, 2, -3)

    def test_size_zero(self):
        """A size of zero raises ValueError."""
        with self.assertRaises(ValueError):
            Square(0)

    def test_str(self):
        """__str__ produces the expected format."""
        s = Square(5, 1, 2, 12)
        self.assertEqual(str(s), "[Square] (12) 1/2 - 5")

    def test_to_dictionary(self):
        """to_dictionary() returns the expected dict."""
        s = Square(5, 1, 2, 99)
        expected = {"id": 99, "size": 5, "x": 1, "y": 2}
        self.assertEqual(s.to_dictionary(), expected)

    def test_update_args(self):
        """update() with positional args in id/size/x/y order."""
        s = Square(1)
        s.update(89, 2, 3, 4)
        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 2)
        self.assertEqual(s.x, 3)
        self.assertEqual(s.y, 4)

    def test_update_kwargs(self):
        """update() with keyword arguments."""
        s = Square(1)
        s.update(size=10)
        self.assertEqual(s.size, 10)


if __name__ == "__main__":
    unittest.main()
