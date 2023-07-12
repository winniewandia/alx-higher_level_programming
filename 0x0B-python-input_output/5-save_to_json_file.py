#!/usr/bin/python3
"""This module contains the save_to_json_file function
"""
import json


def save_to_json_file(my_obj, filename):
    """function that writes an Object to a text file,
    using a JSON representation

    Args:
        my_obj (obj): object to be added to textfile
        filename (str): name of file
    """
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
