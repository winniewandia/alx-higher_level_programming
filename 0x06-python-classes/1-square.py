#!/usr/bin/python3
"""This is a module called 1-square.

The module contains a class Square that contains a
private attribute size
"""


class Square:
    """The class Square defines a square.
    """

    def __init__(self, size):
        """ The __init__ method initializes the size attribute

        Args:
            attr1(int): This desribes the size of one side
        """
        self.__size = size
