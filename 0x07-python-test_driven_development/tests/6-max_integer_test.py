#!/usr/bin/python3
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_none(self):
        self.assertEqual(max_integer([]), None)

    def test_zero(self):
        self.assertEqual(max_integer([0]), 0)

    def test_maxint(self):
        self.assertEqual(max_integer([-2, -100, 5, 0, 10]), 10)

    def test_negative(self):
        self.assertEqual(max_integer([-2, -4, -10, -1]), -1)

    def test_single_list(self):
        self.assertEqual(max_integer([1]), 1)

    def test_repeated_list(self):
        self.assertEqual(max_integer([50, 50, 50]), 50)

    def test_expression(self):
        self.assertEqual(max_integer([0, 5, -6 * -6, 2]), 36)

    def test_max_start(self):
        self.assertEqual(max_integer([100, 2, 7, 50]), 100)

    def test_string(self):
        self.assertRaises(TypeError, max_integer, [1, '1'])

    def test_number(self):
        self.assertRaises(TypeError, max_integer, 1)

    def test_tuple(self):
        self.assertRaises(TypeError, max_integer, [0, (1, 2, 3, 4)])

    def test_dictionary(self):
        self.assertRaises(TypeError, max_integer, [
                          5, {'age': 25, 'likes': 10}])
