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
        """returns the JSON string representation of list_dictionaries

        Args:
            list_dictionaries (list): list of dictionaries

        Returns:
            Json string: JSON string representation of list_dictionaries
        """
        if list_dictionaries is None or list_dictionaries == "[]":
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file

        Args:
            list_objs (list): is a list of instances
        """
        filename = "{}.json".format(cls.__name__)
        my_list = []
        if list_objs is None:
            pass
        else:
            for i in range(len(list_objs)):
                my_list.append(list_objs[i].to_dictionary())
        json_rep = cls.to_json_string(my_list)
        with open(filename, 'w', encoding="utf-8") as f:
            f.write(json_rep)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string

        Args:
            json_string (str): string representing a list of dictionaries

        Returns:
            list: the list of the JSON string representation
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set

        Returns:
            instance: instance with all attributes already set
        """
        if cls.__name__ == "Rectangle":
            new = cls(10, 10)
        else:
            new = cls(10)
        new.update(**dictionary)
        return new
