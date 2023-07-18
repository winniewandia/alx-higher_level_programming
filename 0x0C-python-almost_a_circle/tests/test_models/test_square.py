#!/usr/bin/python3
"""This module contains the class TestSquareMethods
"""
from io import StringIO
import unittest
from unittest.mock import patch
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

    def test_attr(self):
        """Test the size, height, and width of square with
        one attribute
        """
        new = Square(1)
        self.assertEqual(new.size, 1)
        self.assertEqual(new.height, 1)
        self.assertEqual(new.width, 1)
        self.assertEqual(new.x, 0)
        self.assertEqual(new.y, 0)
        self.assertEqual(new.id, 1)

    def test_all_attr(self):
        """Test all attributes with all arguments
        """
        new = Square(1, 2, 3, 4)
        self.assertEqual(new.size, 1)
        self.assertEqual(new.height, 1)
        self.assertEqual(new.width, 1)
        self.assertEqual(new.x, 2)
        self.assertEqual(new.y, 3)
        self.assertEqual(new.id, 4)

    def test_two_squares(self):
        """Test if 2 Squares are the same object
        """
        new = Square(1, 1)
        new2 = Square(1, 1)
        self.assertEqual(False, new is new2)
        self.assertEqual(False, new.id == new2.id)

    def test_rect_inst(self):
        """Test if square is an instance of rectangle
        """
        new = Square(1)
        self.assertEqual(True, isinstance(new, Rectangle))

    def test_base_inst(self):
        """Test if square is an instance of base
        """
        new = Square(1)
        self.assertEqual(True, isinstance(new, Base))

    def test_priv_width(self):
        """Trying to access private variable width
        """
        new = Square(1)
        with self.assertRaises(AttributeError):
            new.__width

    def test_priv_height(self):
        """Trying to access private variable height
        """
        new = Square(1)
        with self.assertRaises(AttributeError):
            new.__height

    def test_priv_x(self):
        """Trying to access private variable x
        """
        new = Square(1)
        with self.assertRaises(AttributeError):
            new.__x

    def test_priv_y(self):
        """Trying to access private variable y
        """
        new = Square(1)
        with self.assertRaises(AttributeError):
            new.__y

    def test_string_size(self):
        """Passing size as string
        """
        with self.assertRaises(TypeError):
            new = Square('1', 2, 3, 4)

    def test_string_x(self):
        """Passing x as string
        """
        with self.assertRaises(TypeError):
            new = Square(1, '2', 3, 4)

    def test_string_y(self):
        """Passing y as string
        """
        with self.assertRaises(TypeError):
            new = Square(1, 2, '3', 4)

    def test_negative_size(self):
        """Passing size as negative
        """
        with self.assertRaises(ValueError):
            new = Square(-1, 2, 3, 4)

    def test_zero_size(self):
        """Passing size as 0
        """
        with self.assertRaises(ValueError):
            new = Square(0, 2, 3, 4)

    def test_square_dict(self):
        """Test for dictionary representation of Square
        """
        s1 = Square(10, 2, 1)
        s1_dictionary = s1.to_dictionary()
        out = "<class 'dict'>\n"
        with patch('sys.stdout', StringIO()) as mock_output:
            print(type(s1_dictionary))
            self.assertEqual(mock_output.getvalue(), out)

        s2 = Square(1, 1)
        s2.update(**s1_dictionary)
        self.assertEqual(False, s1 == s2)
