#!/usr/bin/python3
"""This is the Lookup module that contains
the lookup function
"""


def lookup(obj):
    """function that returns the list of available attributes
    and methods of an object

    Args:
        obj (object): instance of the class

    Returns:
        a list object
    """
    return dir(obj)
