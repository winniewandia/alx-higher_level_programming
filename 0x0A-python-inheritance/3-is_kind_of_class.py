#!/usr/bin/python3
"""This module contains the is_kind_of_class
"""


def is_kind_of_class(obj, a_class):
    """a function that returns True if the object is an
    instance of, or if the object is an instance of a class
    that inherited from, the specified class ; otherwise False

    Args:
        obj (object): object to be checked
        a_class (class): class to be checked against

    Returns:
        _type_: true if they object is an instance of class
    """
    return isinstance(obj, a_class)
