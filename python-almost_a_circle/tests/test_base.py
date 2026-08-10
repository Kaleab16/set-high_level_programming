#!/usr/bin/python3
"""Unittest for the Base class."""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Tests for Base."""

    def test_id_auto_assigned(self):
        """First Base() gets an id, increasing from previous state."""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id, b1.id + 1)

    def test_id_passed_in(self):
        """Passing an explicit id uses that value directly."""
        b = Base(89)
        self.assertEqual(b.id, 89)

    def test_to_json_string_none(self):
        """None becomes '[]'."""
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string_empty_list(self):
        """Empty list becomes '[]'."""
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_with_data(self):
        """A list of dicts serializes to a JSON string."""
        self.assertEqual(
            Base.to_json_string([{'id': 12}]), '[{"id": 12}]')

    def test_to_json_string_returns_str(self):
        """The return value type is str."""
        result = Base.to_json_string([{'id': 12}])
        self.assertEqual(type(result), str)

    def test_from_json_string_none(self):
        """None becomes an empty list."""
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_string_empty(self):
        """'[]' becomes an empty list."""
        self.assertEqual(Base.from_json_string("[]"), [])

    def test_from_json_string_with_data(self):
        """A JSON string parses back into a list of dicts."""
