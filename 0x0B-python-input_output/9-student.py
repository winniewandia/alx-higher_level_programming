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

    def to_json(self):
        """retrieves a dictionary representation of a Student instance

        Returns:
            dictionary representation of a Student instance
        """
        return self.__dict__.copy()
