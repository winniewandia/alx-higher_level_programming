#!/usr/bin/python3
"""This module contains the class_to_json function
"""


def class_to_json(obj):
    """function that returns the dictionary description with
    simple data structure (list, dictionary, string, integer
    and boolean) for JSON serialization of an object

    Args:
        obj: an instance of a Class

    Returns:
        returns the dictionary description with simple data structure
    """
    src = {}
    if hasattr(obj, "__dict__"):
        src = obj.__dict__.copy()
    return src
