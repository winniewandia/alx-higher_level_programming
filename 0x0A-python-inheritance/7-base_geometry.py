#!/usr/bin/python3
"""This module contains the class BaseGeometry that
    contains a function area that raises an Exception

    Raises:
        Exception: if area is not implemented
"""


class BaseGeometry:
    """The BaseGeometry class contains a function area that
    raises an exception
    """

    def area(self):
        """This area function raises an exception

        Raises:
            Exception: raised if the area is not defined
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Public instance method that validates value

        Args:
            name (str): string
            value (int): integer to be validated

        Raises:
            TypeError: if value is not an int
            ValueError: if value <= 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
