#!/usr/bin/python3
"""This module is called 2-square.

It contains a class Square with private size attribute
that raises TypeError and ValueError
"""


class Square:
    """The class Square defines a square with
    private instance size.
    """

    def __init__(self, size=0, position=(0, 0)):
        """This initializes the size of the square
        Attributes:
        size(int): The size of the square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """This method gets the size property.
        The setter method below sets the value of size
        depending on whether its an int or greater than 0
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """This method gets the position property.
        The setter method below sets the value of position
        depending on whether its a tuple of 2 int"""
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """This method computes the area of a square
        using its size
        """
        return int(self.__size) * int(self.__size)

    def my_print(self):
        """This method prints the square to stdout
        using # for each size
        """
        if not self.__size:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("{}".format("#"), end='')
                print()
