#!/usr/bin/python3
"""This module contains the class Base
"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """eturns the JSON string representation of list_dictionaries

        Args:
            list_dictionaries (list): list of dictionaries

        Returns:
            Json string: JSON string representation of list_dictionaries
        """
        if list_dictionaries is None or list_dictionaries == "[]":
            return "[]"
        return json.dumps(list_dictionaries)
