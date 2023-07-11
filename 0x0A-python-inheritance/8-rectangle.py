#!/usr/bin/python3
"""This module contains the class Rectangle that inherits
BaseGeometry
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class Rectangle that inherits BaseGeometry

    Args:
        BaseGeometry (class): Parent class
    """

    def __init__(self, width, height):
        """Instantiation with width and height

        Args:
            width (int): rectangle's width
            height (int): rectangle's height
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
