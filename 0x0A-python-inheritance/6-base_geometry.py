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
