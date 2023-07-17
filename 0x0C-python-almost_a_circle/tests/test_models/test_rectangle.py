#!/usr/bin/python3
"""This module contains the TestRectangleMethods class
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from io import StringIO
from unittest.mock import patch


class TestRectangleMethods(unittest.TestCase):
    """This class contains the suite for rectangle methods
    """

    def setUp(self):
        """This method initializes the Base__nb_objects
        to 0
        """
        Base._Base__nb_objects = 0

    def test_zero_attr(self):
        """Raises attribute error when no args are given"""
        with self.assertRaises(TypeError):
            new = Rectangle()

    def test_single_attr(self):
        """Raises attribute error when 1 arg is given
        """
        with self.assertRaises(TypeError):
            new = Rectangle(1)

    def test_rectangle(self):
        """Test rectangle with required args
        """
        new = Rectangle(1, 1)
        self.assertEqual(new.height, 1)
        self.assertEqual(new.width, 1)
        self.assertEqual(new.x, 0)
        self.assertEqual(new.y, 0)
        self.assertEqual(new.id, 1)

    def test_all_args(self):
        """Tests rectangle with all args given
        """
        new = Rectangle(1, 1, 1, 1, 1)
        self.assertEqual(new.height, 1)
        self.assertEqual(new.width, 1)
        self.assertEqual(new.x, 1)
        self.assertEqual(new.y, 1)
        self.assertEqual(new.id, 1)

    def test_instance(self):
        """Test Rectangle is a Base instance
        """
        new = Rectangle(1, 1)
        self.assertEqual(True, isinstance(new, Base))

    def test_equality(self):
        """Tests if 2 instances are the same object
        """
        new = Rectangle(1, 1)
        new2 = Rectangle(1, 1)
        self.assertEqual(False, new is new2)
        self.assertEqual(False, new.id == new2.id)

    def test_access_width(self):
        """Raises attribute error if private attribute width is
        accessed
        """
        new = Rectangle(1, 1)
        with self.assertRaises(AttributeError):
            new.__width

    def test_access_height(self):
        """Raises attribute error if private attribute height is
        accessed
        """
        new = Rectangle(1, 1)
        with self.assertRaises(AttributeError):
            new.__height

    def test_access_x(self):
        """Raises attribute error if private attribute x is
        accessed
        """
        new = Rectangle(1, 1)
        with self.assertRaises(AttributeError):
            new.__x

    def test_access_y(self):
        """Raises attribute error if private attribute y is
        accessed
        """
        new = Rectangle(1, 1)
        with self.assertRaises(AttributeError):
            new.__y

    def test_string_width(self):
        """Raises TypeError if width is not an int
        """
        with self.assertRaises(TypeError):
            new = Rectangle('1', 1, 1, 1, 1)

    def test_string_height(self):
        """Raises TypeError if height is not an int
        """
        with self.assertRaises(TypeError):
            new = Rectangle(1, '1', 1, 1, 1)

    def test_string_x(self):
        """Raises TypeError if x is not an int
        """
        with self.assertRaises(TypeError):
            new = Rectangle(1, 1, '1', 1, 1)

    def test_string_y(self):
        """Raises TypeError if y is not an int
        """
        with self.assertRaises(TypeError):
            new = Rectangle(1, 1, 1, '1', 1)

    def test_height_zero(self):
        """Raises ValueError if height and weight is <= 0
        """
        with self.assertRaises(ValueError):
            new = Rectangle(0, -4)

    def test_xy_negative(self):
        """Raises ValueError if x and y is < 0
        """
        with self.assertRaises(ValueError):
            new = Rectangle(1, 1, -2, -3, 1)

    def test_area(self):
        """Tests area of a rectangle
        """
        new = Rectangle(1, 2)
        self.assertEqual(new.area(), 2)
        new2 = Rectangle(3, 4)
        self.assertEqual(new2.area(), 12)

    def test_area2(self):
        """Tests for area if height and width are modified
        """
        new = Rectangle(5, 6)
        self.assertEqual(new.area(), 30)
        new.width = 2
        self.assertEqual(new.area(), 12)
        new.height = 3
        self.assertEqual(new.area(), 6)

    def test_display(self):
        """Test display
        """
        new = Rectangle(2, 3)
        out = "##\n##\n##\n"
        with patch('sys.stdout', io_out=StringIO()) as str:
            new.display()
            self.assertEqual(str.getvalue(), out)

    def test_display_change(self):
        """Test display with height changed
        """
        new = Rectangle(2, 3)
        out = "##\n##\n##\n"
        with patch('sys.stdout', io_out=StringIO()) as str:
            new.display()
            self.assertEqual(str.getvalue(), out)

        new.height = 2
        out = "##\n##\n"
        with patch('sys.stdout', io_out=StringIO()) as str:
            new.display()
            self.assertEqual(str.getvalue(), out)

    def test_str_print(self):
        """Tests str method print value
        """
        new = Rectangle(1, 2, 3, 4, 5)
        out = "[Rectangle] (5) 3/4 - 1/2"
        with patch('sys.stdout', io_out=StringIO()) as str:
            print(new)
            self.assertEqual(str.getvalue(), out)

    def test_str_return(self):
        "Test str return value"
        new = Rectangle(1, 2, 3, 4, 5)
        out = "[Rectangle] (5) 3/4 - 1/2"
        self.assertEqual(new.__str__, out)
