#!/usr/bin/python3
"""
This module contains unittest for /models/base.py
"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """This class TestBase defines tests for class Base methods"""

    def test00_int(self):
        """Test valid id attribute"""
        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base(12)
        b5 = Base(-1)
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)
        self.assertEqual(b4.id, 12)
        self.assertEqual(b5.id, -1)

    def test01_none(self):
        """Test None input"""
        b6 = Base(None)
        self.assertEqual(b6.id, 3)

    def test02_float(self):
        """Test float input"""
        b7 = Base(1.2)
        self.assertEqual(b7.id, 1.2)

    def test03_string(self):
        """Test string input"""
        b8 = Base("covid19¯\\_(ツ)_/¯")
        self.assertEqual(b8.id, "covid19¯\\_(ツ)_/¯")

    def test04_list(self):
        """Test list input"""
        b9 = Base([10, 11, 12])
        self.assertEqual(b9.id, [10, 11, 12])

    def test05_tuple(self):
        """Test tuple input"""
        b10 = Base((10, 11, 12))
        self.assertEqual(b10.id, (10, 11, 12))

if __name__ == '__main__':
    unittest.main()
