#!/usr/bin/python3
"""Module for Square unit tests"""
import unittest
import io
import sys
from models.base import Base
from models.square import Square


class TestSquare(unittest.TestCase):

    def test_size_validation(self):
        """
        test size value
        """
        with self.assertRaises(TypeError):
            s = Square("invalid")
        with self.assertRaises(ValueError):
            s = Square(-5)


if __name__ == '__main__':
    unittest.main()
