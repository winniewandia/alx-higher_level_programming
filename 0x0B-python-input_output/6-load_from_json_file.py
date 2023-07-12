#!/usr/bin/python3
"""This module contains the load_from_json_file function
"""
import json


def load_from_json_file(filename):
    """function that creates an Object from a “JSON file”

    Args:
        filename: name of file
    """
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
