#!/usr/bin/python3
"""Unit tests for Square class"""
import unittest
import json
import os
import sys
from io import StringIO
from models.square import Square
from models.base import Base
from models.rectangle import Rectangle


class TestSquare(unittest.TestCase):
    """Test cases for Square class"""

    def setUp(self):
        """Set up test environment"""
        Base._Base__nb_objects = 0

    def tearDown(self):
        """Clean up after tests"""
        if os.path.exists("Square.json"):
            os.remove("Square.json")

    def test_square_creation(self):
        """Test Square creation with various parameters"""
        s1 = Square(5, 1, 2, 12)
        self.assertEqual(s1.id, 12)
        self.assertEqual(s1.size, 5)
        self.assertEqual(s1.width, 5)
        self.assertEqual(s1.height, 5)
        self.assertEqual(s1.x, 1)
        self.assertEqual(s1.y, 2)
        
        s2 = Square(4, 0, 0, 5)
        self.assertEqual(s2.id, 5)
        self.assertEqual(s2.size, 4)
        self.assertEqual(s2.x, 0)
        self.assertEqual(s2.y, 0)
        
        s3 = Square(3)
        self.assertEqual(s3.id, 1)
        self.assertEqual(s3.size, 3)
        self.assertEqual(s3.x, 0)
        self.assertEqual(s3.y, 0)

    def test_size_validation(self):
        """Test size validation"""
        with self.assertRaises(ValueError) as e:
            Square(-5)
        self.assertEqual(str(e.exception), "width must be > 0")
        
        with self.assertRaises(ValueError) as e:
            Square(0)
        self.assertEqual(str(e.exception), "width must be > 0")
        
        with self.assertRaises(TypeError) as e:
            Square("5")
        self.assertEqual(str(e.exception), "width must be an integer")
        
        with self.assertRaises(TypeError) as e:
            Square(5.5)
        self.assertEqual(str(e.exception), "width must be an integer")

    def test_x_validation_square(self):
        """Test x validation for Square"""
        with self.assertRaises(ValueError) as e:
            Square(5, -1)
        self.assertEqual(str(e.exception), "x must be >= 0")
        
        with self.assertRaises(TypeError) as e:
            Square(5, "1")
        self.assertEqual(str(e.exception), "x must be an integer")

    def test_y_validation_square(self):
        """Test y validation for Square"""
        with self.assertRaises(ValueError) as e:
            Square(5, 1, -1)
        self.assertEqual(str(e.exception), "y must be >= 0")
        
        with self.assertRaises(TypeError) as e:
            Square(5, 1, "1")
        self.assertEqual(str(e.exception), "y must be an integer")

    def test_area_square(self):
        """Test area method for Square"""
        s1 = Square(4)
        self.assertEqual(s1.area(), 16)
        
        s2 = Square(6, 1, 1, 7)
        self.assertEqual(s2.area(), 36)
        
        s3 = Square(1)
        self.assertEqual(s3.area(), 1)

    def test_str_square(self):
        """Test __str__ method for Square"""
        s = Square(4, 2, 1, 12)
        self.assertEqual(str(s), "[Square] (12) 2/1 - 4")
        
        s = Square(5, 0, 0, 1)
        self.assertEqual(str(s), "[Square] (1) 0/0 - 5")
        
        s = Square(3, 1, 2, 8)
        self.assertEqual(str(s), "[Square] (8) 1/2 - 3")

    def test_display_square(self):
        """Test display method for Square"""
        s = Square(2)
        expected = "##\n##\n"
        captured_output = StringIO()
        sys.stdout = captured_output
        s.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), expected)
        
        s = Square(2, 1, 1)
        expected = "\n ##\n ##\n"
        captured_output = StringIO()
        sys.stdout = captured_output
        s.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), expected)
        
        s = Square(3, 2, 0)
        expected = "  ###\n  ###\n  ###\n"
        captured_output = StringIO()
        sys.stdout = captured_output
        s.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), expected)

    def test_update_args_square(self):
        """Test update method with *args for Square"""
        s = Square(5, 5, 5, 1)
        
        s.update(89)
        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 5)
        self.assertEqual(s.y, 5)
        
        s.update(89, 2)
        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 2)
        self.assertEqual(s.x, 5)
        self.assertEqual(s.y, 5)
        
        s.update(89, 2, 3)
        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 2)
        self.assertEqual(s.x, 3)
        self.assertEqual(s.y, 5)
        
        s.update(89, 2, 3, 4)
        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 2)
        self.assertEqual(s.x, 3)
        self.assertEqual(s.y, 4)

    def test_update_kwargs_square(self):
        """Test update method with **kwargs for Square"""
        s = Square(5, 5, 5, 1)
        
        s.update(id=90)
        self.assertEqual(s.id, 90)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 5)
        self.assertEqual(s.y, 5)
        
        s.update(id=90, size=6, x=7, y=8)
        self.assertEqual(s.id, 90)
        self.assertEqual(s.size, 6)
        self.assertEqual(s.x, 7)
        self.assertEqual(s.y, 8)
        
        s.update(y=11, x=12, size=13, id=91)
        self.assertEqual(s.id, 91)
        self.assertEqual(s.size, 13)
        self.assertEqual(s.x, 12)
        self.assertEqual(s.y, 11)

    def test_to_dictionary_square(self):
        """Test to_dictionary method for Square"""
        s = Square(10, 2, 3, 5)
        expected = {'id': 5, 'size': 10, 'x': 2, 'y': 3}
        self.assertEqual(s.to_dictionary(), expected)
        self.assertEqual(type(s.to_dictionary()), dict)
        
        s = Square(1, 0, 0, 1)
        expected = {'id': 1, 'size': 1, 'x': 0, 'y': 0}
        self.assertEqual(s.to_dictionary(), expected)

    def test_square_inheritance(self):
        """Test that Square inherits from Rectangle and Base"""
        s = Square(5)
        self.assertIsInstance(s, Rectangle)
        self.assertIsInstance(s, Base)
        self.assertTrue(issubclass(Square, Rectangle))
        self.assertTrue(issubclass(Square, Base))

    def test_square_size_property(self):
        """Test that size property works correctly"""
        s = Square(5)
        self.assertEqual(s.size, 5)
        
        s.size = 10
        self.assertEqual(s.size, 10)
        self.assertEqual(s.width, 10)
        self.assertEqual(s.height, 10)
        
        with self.assertRaises(ValueError) as e:
            s.size = -1
        self.assertEqual(str(e.exception), "width must be > 0")
        
        with self.assertRaises(TypeError) as e:
            s.size = "10"
        self.assertEqual(str(e.exception), "width must be an integer")


if __name__ == '__main__':
    unittest.main()
