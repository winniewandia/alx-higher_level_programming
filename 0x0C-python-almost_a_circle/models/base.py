#!/usr/bin/python3
"""This module contains the class Base
"""


class Base:
    """This class contains the private class attribute
    __nb_objects and class constructor initializing id
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """This method initializes class instances

        Args:
            id (int, optional): the id. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
