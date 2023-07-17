#!/usr/bin/python3
"""This test module contains the class
    TestBaseMethods
"""
import unittest
from models.base import Base


class TestBaseMethods(unittest.TestCase):
    """This class contains the test suite for the Base class
    """

    def setUp(self):
        """Initialize Base__nb_objects
        """
        Base._Base__nb_objects = 0

    def test_int_id(self):
        """Test id with string
        """
        new = Base(1)
        self.assertEqual(new.id, 1)

    def test_default(self):
        """Test id with None"""
        new = Base()
        self.assertEqual(new.id, 1)

    def test_mix(self):
        """Test several id arguments
        """
        new = Base()
        new1 = Base(1)
        new2 = Base(2)
        new3 = Base()
        self.assertEqual(new.id, 1)
        self.assertEqual(new1.id, 1)
        self. assertEqual(new2.id, 2)
        self. assertEqual(new3.id, 2)

    def test_string(self):
        """Tests string id
        """
        new = Base('2')
        self.assertEqual(new.id, '2')

    def test_more_args(self):
        """Test id when more than one args are given
        """
        with self.assertRaises(TypeError):
            new = Base(2, 2)

    def test_private_attr(self):
        """Raise exception when trying to access private attribute
        """
        new = Base()
        with self.assertRaises(AttributeError):
            new.__nb_objects
