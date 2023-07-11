#!/usr/bin/python3
"""This module contains the to_json_string function

    Returns:
        json string: json string representation of my_obj
"""
import json


def to_json_string(my_obj):
    """function that returns the JSON representation of an object (string)

    Args:
        my_obj (object): object to ba changed to string

    Returns:
        json string: json string representation of my_obj
    """
    return json.dumps(my_obj)
