#!/usr/bin/python3
"""This is_same_class contains the is_same_class function
"""


def is_same_class(obj, a_class):
    """function that returns True if the object
    is exactly an instance of the specified class,
    otherwise False

    Args:
        obj (obj): object to be checked
        a_class (class): the class to compare

    Returns:
        _type_: true if they are of the same class
    """
    return type(obj) is a_class
