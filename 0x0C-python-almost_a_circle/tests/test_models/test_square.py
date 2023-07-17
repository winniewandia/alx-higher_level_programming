#!/usr/bin/python3
"""This module contains the class TestSquareMethods
"""
import unittest
from models.square import Square
from models.rectangle import Rectangle
from models.base import Base


class TestSquareMethods(unittest.TestCase):
    """class TestSquareMethods contains the test suite

    Args:
        unittest (class): base class
    """

    def setUp(self):
        """This method initializes the Base__nb_objects
        to 0
        """
        Base._Base__nb_objects = 0

    def test_zero_attr(self):
        """Raises attribute error when no args are given"""
        with self.assertRaises(TypeError):
            new = Square()
