#!/usr/bin/python3
"""This module contains the from_json_string function
"""
import json


def from_json_string(my_str):
    """function that returns an object (Python
    data structure) represented by a JSON string

    Args:
        my_str (str): string to be decoded to object

    Returns:
        obj: decoded object
    """
    return json.loads(my_str)
