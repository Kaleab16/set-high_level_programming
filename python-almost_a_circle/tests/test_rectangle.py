#!/usr/bin/python3
"""Unittest for the Rectangle class."""
import os
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

    def test_display_no_x_no_y(self):
        """display() with default x=0, y=0."""
        r = Rectangle(3, 3)
        r.display()

    def test_display_no_y(self):
        """display() with a custom x but default y=0."""
        r = Rectangle(3, 3, 2)
        r.display()

    def test_display_with_x_and_y(self):
        """display() with both x and y set."""
        r = Rectangle(3, 3, 2, 2)
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

    def test_create(self):
        """create() builds an instance from a dictionary."""
        r = Rectangle.create(**{'id': 89, 'width': 1,
                                 'height': 2, 'x': 3, 'y': 4})
        self.assertEqual(r.to_dictionary(),
                          {'id': 89, 'width': 1,
                           'height': 2, 'x': 3, 'y': 4})

    def test_save_to_file_none(self):
        """save_to_file(None) creates an empty-list JSON file."""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_empty_list(self):
        """save_to_file([]) creates an empty-list JSON file."""
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_with_data(self):
        """save_to_file() writes valid JSON data to disk."""
        r = Rectangle(3, 5, 1, 2, 10)
        Rectangle.save_to_file([r])
        with open("Rectangle.json", "r") as f:
            content = f.read()
        self.assertIn('"id": 10', content)

    def test_load_from_file_no_file(self):
        """load_from_file() returns [] when the file doesn't exist."""
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_load_from_file_with_data(self):
        """load_from_file() reconstructs saved instances."""
        r = Rectangle(3, 5, 1, 2, 10)
        Rectangle.save_to_file([r])
        loaded = Rectangle.load_from_file()
        self.assertEqual(loaded[0].to_dictionary(), r.to_dictionary())


if __name__ == "__main__":
    unittest.main()
