#!/usr/bin/python3
"""Unittest for the Rectangle class."""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Tests for Rectangle."""

    def test_basic_creation(self):
        """A basic Rectangle(1, 2) is created without error."""
        r = Rectangle(1, 2)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)

    def test_with_x(self):
        """Rectangle(1, 2, 3) sets x."""
        r = Rectangle(1, 2, 3)
        self.assertEqual(r.x, 3)

    def test_with_x_and_y(self):
        """Rectangle(1, 2, 3, 4) sets x and y."""
        r = Rectangle(1, 2, 3, 4)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)

    def test_width_not_int(self):
        """A non-integer width raises TypeError."""
        with self.assertRaises(TypeError):
            Rectangle("1", 2)

    def test_height_not_int(self):
        """A non-integer height raises TypeError."""
        with self.assertRaises(TypeError):
            Rectangle(1, "2")

    def test_x_not_int(self):
        """A non-integer x raises TypeError."""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, "3")

    def test_y_not_int(self):
        """A non-integer y raises TypeError."""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, "4")

    def test_width_negative(self):
        """A negative width raises ValueError."""
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)

    def test_height_negative(self):
        """A negative height raises ValueError."""
        with self.assertRaises(ValueError):
            Rectangle(1, -2)

    def test_width_zero(self):
        """A width of zero raises ValueError."""
        with self.assertRaises(ValueError):
            Rectangle(0, 2)

    def test_height_zero(self):
        """A height of zero raises ValueError."""
        with self.assertRaises(ValueError):
            Rectangle(1, 0)

    def test_x_negative(self):
        """A negative x raises ValueError."""
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -3)

    def test_y_negative(self):
        """A negative y raises ValueError."""
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, -4)

    def test_area(self):
        """area() returns width * height."""
        r = Rectangle(3, 5)
        self.assertEqual(r.area(), 15)

    def test_str(self):
        """__str__ produces the expected format."""
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")

    def test_display_basic(self):
        """display() runs without error for a plain rectangle."""
        r = Rectangle(2, 2)
        r.display()

    def test_to_dictionary(self):
        """to_dictionary() returns the expected dict."""
        r = Rectangle(3, 4, 1, 2, 99)
        expected = {"id": 99, "width": 3, "height": 4, "x": 1, "y": 2}
        self.assertEqual(r.to_dictionary(), expected)

    def test_update_args(self):
        """update() with positional args in id/width/height/x/y order."""
        r = Rectangle(1, 1)
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 4)
        self.assertEqual(r.y, 5)

    def test_update_kwargs(self):
        """update() with keyword arguments."""
        r = Rectangle(1, 1)
        r.update(width=10, height=20)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 20)


if __name__ == "__main__":
    unittest.main()
