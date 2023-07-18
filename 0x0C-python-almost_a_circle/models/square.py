#!/usr/bin/python3
"""This module contains the class Square
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square inherits from class Rectangle

    Args:
        Rectangle (class): parent class
    """

    def __init__(self, size, x=0, y=0, id=None):
        """inherits from the rectangle

        Args:
            size (int): size of square
            x (int, optional): Defaults to 0.
            y (int, optional): Defaults to 0.
            id (_type_, optional): Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Informal string representation

        Returns:
            str: string representation
        """
        rect = "[Square] "
        ids = "({}) ".format(self.id)
        xy = "{}/{} - ".format(self.x, self.y)
        wh = "{}".format(self.size)
        return rect + ids + xy + wh

    @property
    def size(self):
        """This method gets the width property

        Returns:
            int: the width
        """
        return self.width

    @size.setter
    def size(self, value):
        """This method sets the width value

        Args:
            value (int): the width of the rectangle
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Public method that assigns attributes
        """
        if args is not None and len(args) is not 0:
            my_list = ['id', 'size', 'x', 'y']
            for i in range(len(args)):
                setattr(self, my_list[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """returns the dictionary representation of a Square

        Returns:
            dict: dictionary representation of a Square
        """
        my_list = ['id', 'size', 'x', 'y']
        my_dict = {}

        for key in my_list:
            my_dict[key] = getattr(self, key)
        return my_dict
