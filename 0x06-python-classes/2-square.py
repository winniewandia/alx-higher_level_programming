#!/usr/bin/python3
"""This module is called 2-square.

It contains a class Square with private size attribute
that raises TypeError and ValueError
"""


class Square:
    """The class Square defines a square with
    private instance size."""

    def __init__(self, size=0):
        """This initializes the size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = int(size)
