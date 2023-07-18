#!/usr/bin/python3
"""This module contains the Rectangle class thar
inherits from Base class

Returns:
    int: the set attribute values
"""
from models.base import Base


class Rectangle(Base):
    """class Rectangle that inherits from Base.
    Contains Private instance attributes, each with
    its own public getter and setter

    Args:
        Base (class): The inherited class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes the width, height, x, y, id of each
        instance

        Args:
            width (int): width of the Rectangle
            height (int): height of the rectangle
            x (int, optional):  Defaults to 0.
            y (int, optional):  Defaults to 0.
            id (int, optional): the id. Defaults to None.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """This method gets the width property

        Returns:
            int: the width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """This method sets the width value

        Args:
            value (int): the width of the rectangle

        Raises:
            TypeError: if width is not an int
            ValueError: if width is <= 0
        """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        """This method gets the height value

        Returns:
            int: height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """This method sets the height value

        Args:
            value (int): height of the rectangle

        Raises:
            TypeError: if height is not an int
            ValueError: if height is <= 0
        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        """This method gets the x property

        Returns:
            int: x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """This method sets the x value

        Args:
            value (int): value of x

        Raises:
            TypeError: if x is not an int
        """
        if type(value) is not int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        """This method gets the y property

        Returns:
            int: y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """This method sets the y value

        Args:
            value (int): value of y
        Raises:
            TypeError: if y is not an int
        """
        if not isinstance(value, int):
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """returns the area value of the Rectangle instance.

        Returns:
            int: Area of the Rectangle
        """
        return self.__width * self.__height

    def display(self):
        """prints in stdout the Rectangle instance with
        the character #
        """
        for m in range(self.y):
            print()
        for i in range(self.__height):
            print("{}".format(" " * self.x), end='')
            for j in range(self.__width):
                print("{}".format("#"), end='')
            print()

    def __str__(self):
        """Informal string representation

        Returns:
            str: string representation
        """
        rect = "[Rectangle] "
        ids = "({}) ".format(self.id)
        xy = "{}/{} - ".format(self.x, self.y)
        wh = "{}/{}".format(self.width, self.height)
        return rect + ids + xy + wh

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute
        """
        if args is not None and len(args) != 0:
            list_attr = ["id", "width", "height", "x", "y"]
            for i in range(len(args)):
                setattr(self, list_attr[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle

        Returns:
            dict: dictionary representation of a Rectangle
        """
        my_list = {'id', 'width', 'height', 'x', 'y'}
        my_dict = {}

        for key in my_list:
            my_dict[key] = getattr(self, key)
        return my_dict
