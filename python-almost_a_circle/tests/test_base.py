#!/usr/bin/python3
"""Tests for the Base class."""

import unittest

from models.base import Base


class TestBase(unittest.TestCase):
    """Test cases for Base."""

    def test_id_none(self):
        """Test automatic ID assignment."""
        b1 = Base()
        b2 = Base()

        self.assertEqual(b2.id, b1.id + 1)

    def test_id_value(self):
        """Test manually assigned ID."""
        b = Base(12)

        self.assertEqual(b.id, 12)

    def test_id_string(self):
        """Test string ID."""
        b = Base("12")

        self.assertEqual(b.id, "12")

    def test_id_zero(self):
        """Test zero ID."""
        b = Base(0)

        self.assertEqual(b.id, 0)


if __name__ == "__main__":
    unittest.main()
