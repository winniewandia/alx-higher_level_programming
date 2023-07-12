#!/usr/bin/python3
"""This module contains the class Student
"""


class Student:
    """The class Student contains instatiation and public method
    to_json
    """

    def __init__(self, first_name, last_name, age):
        """Instantiation with first_name, last_name and age

        Args:
            first_name: first name
            last_name: last name
            age: age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance

        Returns:
            dictionary representation of a Student instance
        """
        src = self.__dict__.copy()
        if isinstance(attrs, list):

            for item in attrs:
                if not isinstance(item, str):
                    return src

            my_list = {}

            for i in range(len(attrs)):
                for j in src:
                    if attrs[i] == j:
                        my_list[j] = src[j]
            return my_list

        return src
