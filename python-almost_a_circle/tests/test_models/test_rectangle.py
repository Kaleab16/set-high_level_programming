#!/usr/bin/python3
"""Unit tests for Rectangle class"""
import unittest
import json
import os
import sys
from io import StringIO
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    """Test cases for Rectangle class"""

    def setUp(self):
        """Set up test environment"""
        Base._Base__nb_objects = 0

    def tearDown(self):
        """Clean up after tests"""
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")

    def test_rectangle_creation(self):
        """Test Rectangle creation with various parameters"""
        r1 = Rectangle(10, 2, 1, 3, 12)
        self.assertEqual(r1.id, 12)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 1)
        self.assertEqual(r1.y, 3)
        
        r2 = Rectangle(5, 6, 0, 0, 5)
        self.assertEqual(r2.id, 5)
        self.assertEqual(r2.width, 5)
        self.assertEqual(r2.height, 6)
        self.assertEqual(r2.x, 0)
        self.assertEqual(r2.y, 0)
        
        r3 = Rectangle(3, 4)
        self.assertEqual(r3.id, 1)
        self.assertEqual(r3.width, 3)
        self.assertEqual(r3.height, 4)
        self.assertEqual(r3.x, 0)
        self.assertEqual(r3.y, 0)

    def test_width_validation(self):
        """Test width validation"""
        with self.assertRaises(ValueError) as e:
            Rectangle(-1, 2)
        self.assertEqual(str(e.exception), "width must be > 0")
        
        with self.assertRaises(ValueError) as e:
            Rectangle(0, 2)
        self.assertEqual(str(e.exception), "width must be > 0")
        
        with self.assertRaises(TypeError) as e:
            Rectangle("10", 2)
        self.assertEqual(str(e.exception), "width must be an integer")
        
        with self.assertRaises(TypeError) as e:
            Rectangle(10.5, 2)
        self.assertEqual(str(e.exception), "width must be an integer")

    def test_height_validation(self):
        """Test height validation"""
        with self.assertRaises(ValueError) as e:
            Rectangle(10, -2)
        self.assertEqual(str(e.exception), "height must be > 0")
        
        with self.assertRaises(ValueError) as e:
            Rectangle(10, 0)
        self.assertEqual(str(e.exception), "height must be > 0")
        
        with self.assertRaises(TypeError) as e:
            Rectangle(10, "2")
        self.assertEqual(str(e.exception), "height must be an integer")
        
        with self.assertRaises(TypeError) as e:
            Rectangle(10, 2.5)
        self.assertEqual(str(e.exception), "height must be an integer")

    def test_x_validation(self):
        """Test x validation"""
        with self.assertRaises(ValueError) as e:
            Rectangle(10, 2, -1)
        self.assertEqual(str(e.exception), "x must be >= 0")
        
        with self.assertRaises(TypeError) as e:
            Rectangle(10, 2, "1")
        self.assertEqual(str(e.exception), "x must be an integer")
        
        with self.assertRaises(TypeError) as e:
            Rectangle(10, 2, 1.5)
        self.assertEqual(str(e.exception), "x must be an integer")

    def test_y_validation(self):
        """Test y validation"""
        with self.assertRaises(ValueError) as e:
            Rectangle(10, 2, 1, -1)
        self.assertEqual(str(e.exception), "y must be >= 0")
        
        with self.assertRaises(TypeError) as e:
            Rectangle(10, 2, 1, "1")
        self.assertEqual(str(e.exception), "y must be an integer")
        
        with self.assertRaises(TypeError) as e:
            Rectangle(10, 2, 1, 1.5)
        self.assertEqual(str(e.exception), "y must be an integer")

    def test_area(self):
        """Test area method"""
        r1 = Rectangle(3, 4)
        self.assertEqual(r1.area(), 12)
        
        r2 = Rectangle(5, 6, 1, 1, 7)
        self.assertEqual(r2.area(), 30)
        
        r3 = Rectangle(1, 1)
        self.assertEqual(r3.area(), 1)

    def test_str(self):
        """Test __str__ method"""
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")
        
        r = Rectangle(5, 5, 0, 0, 1)
        self.assertEqual(str(r), "[Rectangle] (1) 0/0 - 5/5")
        
        r = Rectangle(10, 2, 3, 4, 5)
        self.assertEqual(str(r), "[Rectangle] (5) 3/4 - 10/2")

    def test_display(self):
        """Test display method"""
        r = Rectangle(2, 3)
        expected = "##\n##\n##\n"
        captured_output = StringIO()
        sys.stdout = captured_output
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), expected)
        
        r = Rectangle(2, 3, 1, 1)
        expected = "\n ##\n ##\n ##\n"
        captured_output = StringIO()
        sys.stdout = captured_output
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), expected)
        
        r = Rectangle(3, 2, 2, 0)
        expected = "  ###\n  ###\n"
        captured_output = StringIO()
        sys.stdout = captured_output
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), expected)
        
        r = Rectangle(3, 2, 0, 2)
        expected = "\n\n###\n###\n"
        captured_output = StringIO()
        sys.stdout = captured_output
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), expected)

    def test_update_args(self):
        """Test update method with *args"""
        r = Rectangle(10, 10, 10, 10, 1)
        
        r.update(89)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 10)
        self.assertEqual(r.y, 10)
        
        r.update(89, 2)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 10)
        self.assertEqual(r.y, 10)
        
        r.update(89, 2, 3)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 10)
        self.assertEqual(r.y, 10)
        
        r.update(89, 2, 3, 4)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 4)
        self.assertEqual(r.y, 10)
        
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 4)
        self.assertEqual(r.y, 5)

    def test_update_kwargs(self):
        """Test update method with **kwargs"""
        r = Rectangle(10, 10, 10, 10, 1)
        
        r.update(id=90)
        self.assertEqual(r.id, 90)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 10)
        self.assertEqual(r.y, 10)
        
        r.update(id=90, width=6, height=7, x=8, y=9)
        self.assertEqual(r.id, 90)
        self.assertEqual(r.width, 6)
        self.assertEqual(r.height, 7)
        self.assertEqual(r.x, 8)
        self.assertEqual(r.y, 9)
        
        r.update(y=11, x=12, height=13, width=14, id=91)
        self.assertEqual(r.id, 91)
        self.assertEqual(r.width, 14)
        self.assertEqual(r.height, 13)
        self.assertEqual(r.x, 12)
        self.assertEqual(r.y, 11)

    def test_update_args_and_kwargs(self):
        """Test update with both args and kwargs"""
        r = Rectangle(10, 10, 10, 10, 1)
        
        r.update(5, 6, 7, 8, 9, id=100, width=200, height=300, x=400, y=500)
        self.assertEqual(r.id, 5)
        self.assertEqual(r.width, 6)
        self.assertEqual(r.height, 7)
        self.assertEqual(r.x, 8)
        self.assertEqual(r.y, 9)

    def test_to_dictionary(self):
        """Test to_dictionary method"""
        r = Rectangle(10, 2, 1, 9, 5)
        expected = {'id': 5, 'width': 10, 'height': 2, 'x': 1, 'y': 9}
        self.assertEqual(r.to_dictionary(), expected)
        self.assertEqual(type(r.to_dictionary()), dict)
        
        r = Rectangle(1, 1, 0, 0, 1)
        expected = {'id': 1, 'width': 1, 'height': 1, 'x': 0, 'y': 0}
        self.assertEqual(r.to_dictionary(), expected)


if __name__ == '__main__':
    unittest.main()
