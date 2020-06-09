#!/usr/bin/python3
"""
This module contains unittest for /models/rectangle.py
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """This class TestRectangle defines tests for class Rectangle methods"""

    def test00_args(self):
        """Test for valid arguments"""
        r1 = (10, 2, 0, 0, 12)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r1.id, 12)

    def test01_int(self):
        """Test valid id attribute"""
        r2 = Rectangle(10, 2)
        r3 = Rectangle(2, 10)
        r4 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r2.id, 1)
        self.assertEqual(r3.id, 2)
        self.assertEqual(r4.id, 12)

    def test02_width_height(self):
        """Test for valid width & height"""
        r5 = Rectangle(10, 2)
        r6 = Rectangle(2, 10)
        r7 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r5.width, 10)
        self.assertEqual(r5.height, 2)
        self.assertEqual(r6.width, 2)
        self.assertEqual(r6.height, 10)
        self.assertEqual(r7.width, 10)
        self.assertEqual(r7.height, 2)

    def test03_x_y(self):
        """Test for valid x & y"""
        r8 = Rectangle(10, 20)
        r9 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r8.x, 0)
        self.assertEqual(r8.y, 0)
        self.assertEqual(r9.x, 3)
        self.assertEqual(r9.y, 4)

    def test04_none(self):
        """Test with None"""
        with self.assertRaises(TypeError) as e:
            r10 = Rectangle(None)
        self.assertEqual(
            "__init__() missing 1 required positional argument: 'height'",
            str(e.exception))

    def test05_empty(self):
        """Test without arguments"""
        with self.assertRaises(TypeError) as e:
            r11 = Rectangle()
        self.assertEqual(
            "__init__() missing 2 required positional arguments:" +
            "'width' and 'height'",
            str(e.exception))

    def test_nan(self):
        """Test with nan"""

if __name__ == '__main__':
    unittest.main()
