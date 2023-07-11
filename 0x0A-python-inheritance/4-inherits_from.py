#!/usr/bin/python3
"""This module contains the inherits_from function
"""


def inherits_from(obj, a_class):
    """Returns True if the object is an instance of a
    class that inherited (directly or indirectly) from
    the specified class ; otherwise False

    Args:
        obj (object): object to be checked
        a_class (class): class to be checked against

    Returns:
        Boolean: True if the object is an instance of a class
    """
    if type(obj) is a_class:
        return False
    return isinstance(obj, a_class)
