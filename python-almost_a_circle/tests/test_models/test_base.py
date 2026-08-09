#!/usr/bin/python3
"""Unit tests for Base class"""
import unittest
import json
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Test cases for Base class"""

    def setUp(self):
        """Set up test environment"""
        Base._Base__nb_objects = 0

    def tearDown(self):
        """Clean up after tests"""
        for filename in ["Rectangle.json", "Square.json", "Base.json"]:
            if os.path.exists(filename):
                os.remove(filename)

    def test_id_assignment(self):
        """Test automatic and custom id assignment"""
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base()
        self.assertEqual(b3.id, 3)
        
        b4 = Base(12)
        self.assertEqual(b4.id, 12)
        b5 = Base(89)
        self.assertEqual(b5.id, 89)
        
        b6 = Base()
        self.assertEqual(b6.id, 4)
        b7 = Base(100)
        self.assertEqual(b7.id, 100)
        b8 = Base()
        self.assertEqual(b8.id, 5)

    def test_id_string(self):
        """Test string id assignment"""
        b = Base("hello")
        self.assertEqual(b.id, "hello")
        b = Base("12")
        self.assertEqual(b.id, "12")

    def test_id_none(self):
        """Test id assignment with None"""
        b = Base(None)
        self.assertEqual(b.id, 1)
        b = Base(None)
        self.assertEqual(b.id, 2)

    def test_to_json_string(self):
        """Test to_json_string method"""
        list_dicts = [{'id': 1, 'width': 2}, {'id': 2, 'width': 3}]
        json_str = Base.to_json_string(list_dicts)
        self.assertEqual(json_str, json.dumps(list_dicts))
        self.assertEqual(type(json_str), str)
        
        json_str = Base.to_json_string([])
        self.assertEqual(json_str, "[]")
        
        json_str = Base.to_json_string(None)
        self.assertEqual(json_str, "[]")
        
        list_dicts = [{'id': 1}]
        json_str = Base.to_json_string(list_dicts)
        self.assertEqual(json_str, json.dumps(list_dicts))

    def test_from_json_string(self):
        """Test from_json_string method"""
        json_str = '[{"id": 1, "width": 2}, {"id": 2, "width": 3}]'
        list_dicts = Base.from_json_string(json_str)
        expected = [{'id': 1, 'width': 2}, {'id': 2, 'width': 3}]
        self.assertEqual(list_dicts, expected)
        self.assertEqual(type(list_dicts), list)
        
        list_dicts = Base.from_json_string("")
        self.assertEqual(list_dicts, [])
        
        list_dicts = Base.from_json_string(None)
        self.assertEqual(list_dicts, [])
        
        json_str = "[]"
        list_dicts = Base.from_json_string(json_str)
        self.assertEqual(list_dicts, [])

    def test_save_to_file_rectangle(self):
        """Test save_to_file method with Rectangle objects"""
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([r1, r2])
        
        with open("Rectangle.json", "r") as f:
            content = f.read()
        
        expected = json.dumps([r1.to_dictionary(), r2.to_dictionary()])
        self.assertEqual(content, expected)

    def test_save_to_file_square(self):
        """Test save_to_file method with Square objects"""
        s1 = Square(5, 1, 2, 1)
        s2 = Square(3, 0, 0, 2)
        Square.save_to_file([s1, s2])
        
        with open("Square.json", "r") as f:
            content = f.read()
        
        expected = json.dumps([s1.to_dictionary(), s2.to_dictionary()])
        self.assertEqual(content, expected)

    def test_save_to_file_empty_list(self):
        """Test save_to_file with empty list"""
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")
        
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_none(self):
        """Test save_to_file with None"""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")
        
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_append(self):
        """Test that save_to_file overwrites rather than appends"""
        r1 = Rectangle(10, 7, 2, 8, 1)
        Rectangle.save_to_file([r1])
        
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([r2])
        
        with open("Rectangle.json", "r") as f:
            content = f.read()
        
        expected = json.dumps([r2.to_dictionary()])
        self.assertEqual(content, expected)

    def test_create_rectangle(self):
        """Test create method for Rectangle"""
        r_dict = {'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4}
        r = Rectangle.create(**r_dict)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)
        self.assertIsInstance(r, Rectangle)

    def test_create_square(self):
        """Test create method for Square"""
        s_dict = {'id': 89, 'size': 5, 'x': 2, 'y': 3}
        s = Square.create(**s_dict)
        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)
        self.assertIsInstance(s, Square)

    def test_create_with_missing_attributes(self):
        """Test create with missing attributes"""
        r_dict = {'id': 1, 'width': 10, 'height': 20}
        r = Rectangle.create(**r_dict)
        self.assertEqual(r.id, 1)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 20)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    def test_load_from_file_rectangle(self):
        """Test load_from_file method for Rectangle"""
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([r1, r2])
        
        rectangles = Rectangle.load_from_file()
        self.assertEqual(len(rectangles), 2)
        self.assertIsInstance(rectangles[0], Rectangle)
        self.assertEqual(rectangles[0].id, 1)
        self.assertEqual(rectangles[0].width, 10)
        self.assertEqual(rectangles[0].height, 7)
        self.assertEqual(rectangles[0].x, 2)
        self.assertEqual(rectangles[0].y, 8)
        self.assertEqual(rectangles[1].id, 2)
        self.assertEqual(rectangles[1].width, 2)
        self.assertEqual(rectangles[1].height, 4)
        self.assertEqual(rectangles[1].x, 5)
        self.assertEqual(rectangles[1].y, 6)

    def test_load_from_file_square(self):
        """Test load_from_file method for Square"""
        s1 = Square(5, 1, 2, 1)
        s2 = Square(3, 0, 0, 2)
        Square.save_to_file([s1, s2])
        
        squares = Square.load_from_file()
        self.assertEqual(len(squares), 2)
        self.assertIsInstance(squares[0], Square)
        self.assertEqual(squares[0].id, 1)
        self.assertEqual(squares[0].size, 5)
        self.assertEqual(squares[0].x, 1)
        self.assertEqual(squares[0].y, 2)
        self.assertEqual(squares[1].id, 2)
        self.assertEqual(squares[1].size, 3)
        self.assertEqual(squares[1].x, 0)
        self.assertEqual(squares[1].y, 0)

    def test_load_from_file_no_file(self):
        """Test load_from_file when file doesn't exist"""
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        
        rectangles = Rectangle.load_from_file()
        self.assertEqual(rectangles, [])
        
        if os.path.exists("Square.json"):
            os.remove("Square.json")
        
        squares = Square.load_from_file()
        self.assertEqual(squares, [])

    def test_load_from_file_empty_file(self):
        """Test load_from_file with empty file"""
        with open("Rectangle.json", "w") as f:
            f.write("[]")
        
        rectangles = Rectangle.load_from_file()
        self.assertEqual(rectangles, [])


if __name__ == '__main__':
    unittest.main()
