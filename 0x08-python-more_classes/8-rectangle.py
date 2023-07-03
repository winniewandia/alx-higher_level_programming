#!/usr/bin/python3
"""This module is called 0-rectangle.
    It defines a rectangle.
"""


class Rectangle:
    """This defines a class Rectangle with private instance height
    and width.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """This initializes the width and height of the rectangle

        Args:
            width (int, optional): describes the width of rectangle.
            Defaults to 0.
            height (int, optional): defines the height of rectangle.
            Defaults to 0.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """gets the width of the rectangle

        Returns:
            int: rectangle's width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """sets the width of the rectangle.

        Args:
            value (int): the width to be checked

        Raises:
            TypeError: raised if value is not an integer
            ValueError: raised if value is < 0
        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @property
    def height(self):
        """gets the height of the rectangle

        Returns:
            int: the height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """sets the value for the height of the rectangle

        Args:
            value (int): value to be set as height

        Raises:
            TypeError: raised if value is not an integer
            ValueError: raised if value < 0.
        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value

    def area(self):
        """returns the rectangle area

        Returns:
            int: The area of the rectangle
        """
        return self.__height * self.__width

    def perimeter(self):
        """returns the rectangle perimeter

        Returns:
            int: The perimeter if width and height are not 0.
            otherwise 0
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (2 * self.__height) + (2 * self.__width)

    def __str__(self):
        """provides an informal string representation of the rectangle

        Returns:
            str: string representation of a rectangle
        """
        rectangle = ""
        if self.width == 0 or self.height == 0:
            return rectangle
        for i in range(self.height):
            for j in range(self.width):
                rectangle += str(self.print_symbol)
            rectangle += "\n"
        return rectangle[:-1]

    def __repr__(self):
        """Method that returns the string representation of the instance

        Returns:
            str: string representation of the rectangle
        """
        return "Rectangle(" + str(self.width) + ", " + str(self.height) + ")"

    def __del__(self):
        """destroys the instance
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns the biggest rectangle based on the area

        Args:
            rect_1 (int): Area of rect_1
            rect_2 (int): Area of rect_2

        Raises:
            TypeError: if rect_1 is not a Rectangle instace
            TypeError: if rect_2 is not a Rectangle instace

        Returns:
            int: The largest rectangle in terms of area
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
